package "postgresql-server"
package "postgresql"

execute "initdb -D /var/lib/pgsql/data" do
	user "postgres"
  creates "/var/lib/pgsql/data/PG_VERSION"
end

service "postgresql" do
  action [:enable, :start]
end

execute "createdb #{node.postgresql.db_name}" do
  user "postgres"
  not_if(%Q%psql -l | grep "#{node.postgresql.db_name}"%, :user => 'postgres')
end
