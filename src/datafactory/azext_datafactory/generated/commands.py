# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_datafactory.generated._client_factory import cf_factory
    datafactory_factory = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._factory_operations#FactoryOperations.{'
        '}',
        client_factory=cf_factory)
    with self.command_group('datafactory factory', datafactory_factory, client_factory=cf_factory) as g:
        g.custom_command('list', 'datafactory_factory_list')
        g.custom_show_command('show', 'datafactory_factory_show')
        g.custom_command('create', 'datafactory_factory_create')
        g.custom_command('update', 'datafactory_factory_update')
        g.custom_command('delete', 'datafactory_factory_delete')
        g.custom_command('configure-factory-repo', 'datafactory_factory_configure_factory_repo')
        g.custom_command('get-data-plane-access', 'datafactory_factory_get_data_plane_access')
        g.custom_command('get-git-hub-access-token', 'datafactory_factory_get_git_hub_access_token')

    from azext_datafactory.generated._client_factory import cf_exposure_control
    datafactory_exposure_control = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._exposure_control_operations#ExposureCo'
        'ntrolOperations.{}',
        client_factory=cf_exposure_control)
    with self.command_group('datafactory exposure-control', datafactory_exposure_control,
                            client_factory=cf_exposure_control) as g:
        g.custom_command('get-feature-value', 'datafactory_exposure_control_get_feature_value')
        g.custom_command('get-feature-value-by-factory', 'datafactory_exposure_control_get_feature_value_by_factory')

    from azext_datafactory.generated._client_factory import cf_integration_runtime
    datafactory_integration_runtime = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._integration_runtime_operations#Integra'
        'tionRuntimeOperations.{}',
        client_factory=cf_integration_runtime)
    with self.command_group('datafactory integration-runtime', datafactory_integration_runtime,
                            client_factory=cf_integration_runtime) as g:
        g.custom_command('list', 'datafactory_integration_runtime_list')
        g.custom_show_command('show', 'datafactory_integration_runtime_show')
        g.custom_command('managed create', 'datafactory_integration_runtime_managed_create')
        g.custom_command('self-hosted create', 'datafactory_integration_runtime_self_hosted_create')
        g.custom_command('update', 'datafactory_integration_runtime_update')
        g.custom_command('delete', 'datafactory_integration_runtime_delete')
        g.custom_command('create-linked-integration-runtime', 'datafactory_integration_runtime_create_linked_integratio'
                         'n_runtime')
        g.custom_command('get-connection-info', 'datafactory_integration_runtime_get_connection_info')
        g.custom_command('get-monitoring-data', 'datafactory_integration_runtime_get_monitoring_data')
        g.custom_command('get-status', 'datafactory_integration_runtime_get_status')
        g.custom_command('list-auth-key', 'datafactory_integration_runtime_list_auth_key')
        g.custom_command('regenerate-auth-key', 'datafactory_integration_runtime_regenerate_auth_key')
        g.custom_command('remove-link', 'datafactory_integration_runtime_remove_link')
        g.custom_command('start', 'datafactory_integration_runtime_start', supports_no_wait=True)
        g.custom_command('stop', 'datafactory_integration_runtime_stop', supports_no_wait=True)
        g.custom_command('sync-credentials', 'datafactory_integration_runtime_sync_credentials')
        g.custom_command('upgrade', 'datafactory_integration_runtime_upgrade')
        g.wait_command('wait')

    from azext_datafactory.generated._client_factory import cf_integration_runtime_object_metadata
    datafactory_integration_runtime_object_metadata = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._integration_runtime_object_metadata_op'
        'erations#IntegrationRuntimeObjectMetadataOperations.{}',
        client_factory=cf_integration_runtime_object_metadata)
    with self.command_group('datafactory integration-runtime-object-metadata',
                            datafactory_integration_runtime_object_metadata,
                            client_factory=cf_integration_runtime_object_metadata) as g:
        g.custom_command('get', 'datafactory_integration_runtime_object_metadata_get')
        g.custom_command('refresh', 'datafactory_integration_runtime_object_metadata_refresh', supports_no_wait=True)
        g.wait_command('wait')

    from azext_datafactory.generated._client_factory import cf_integration_runtime_node
    datafactory_integration_runtime_node = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._integration_runtime_node_operations#In'
        'tegrationRuntimeNodeOperations.{}',
        client_factory=cf_integration_runtime_node)
    with self.command_group('datafactory integration-runtime-node', datafactory_integration_runtime_node,
                            client_factory=cf_integration_runtime_node) as g:
        g.custom_show_command('show', 'datafactory_integration_runtime_node_show')
        g.custom_command('update', 'datafactory_integration_runtime_node_update')
        g.custom_command('delete', 'datafactory_integration_runtime_node_delete')
        g.custom_command('get-ip-address', 'datafactory_integration_runtime_node_get_ip_address')

    from azext_datafactory.generated._client_factory import cf_linked_service
    datafactory_linked_service = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._linked_service_operations#LinkedServic'
        'eOperations.{}',
        client_factory=cf_linked_service)
    with self.command_group('datafactory linked-service', datafactory_linked_service,
                            client_factory=cf_linked_service) as g:
        g.custom_command('list', 'datafactory_linked_service_list')
        g.custom_show_command('show', 'datafactory_linked_service_show')
        g.custom_command('amazon-m-w-s create', 'datafactory_linked_service_amazon_m_w_s_create')
        g.generic_update_command('amazon-m-w-s update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_amazon_m_w_s_update')
        g.custom_command('amazon-redshift create', 'datafactory_linked_service_amazon_redshift_create')
        g.generic_update_command('amazon-redshift update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_linked_service_amazon_redshift_update')
        g.custom_command('amazon-s3 create', 'datafactory_linked_service_amazon_s3_create')
        g.generic_update_command('amazon-s3 update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_amazon_s3_update')
        g.custom_command('azure-batch create', 'datafactory_linked_service_azure_batch_create')
        g.generic_update_command('azure-batch update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_azure_batch_update')
        g.custom_command('azure-blob-f-s create', 'datafactory_linked_service_azure_blob_f_s_create')
        g.generic_update_command('azure-blob-f-s update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_linked_service_azure_blob_f_s_update')
        g.custom_command('azure-blob-storage create', 'datafactory_linked_service_azure_blob_storage_create')
        g.generic_update_command('azure-blob-storage update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_linked_service_azure_blob_storage_update')
        g.custom_command('azure-data-explorer create', 'datafactory_linked_service_azure_data_explorer_create')
        g.generic_update_command('azure-data-explorer update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_linked_service_azure_data_explorer_update')
        g.custom_command('azure-data-lake-analytics create', 'datafactory_linked_service_azure_data_lake_analytics_crea'
                         'te')
        g.generic_update_command('azure-data-lake-analytics update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_linked_service_azure_data_lake_analytics_update')
        g.custom_command('azure-data-lake-store create', 'datafactory_linked_service_azure_data_lake_store_create')
        g.generic_update_command('azure-data-lake-store update', setter_arg_name = 'properties', custom_func_name = 'da'
                                 'tafactory_linked_service_azure_data_lake_store_update')
        g.custom_command('azure-databricks create', 'datafactory_linked_service_azure_databricks_create')
        g.generic_update_command('azure-databricks update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_linked_service_azure_databricks_update')
        g.custom_command('azure-file-storage create', 'datafactory_linked_service_azure_file_storage_create')
        g.generic_update_command('azure-file-storage update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_linked_service_azure_file_storage_update')
        g.custom_command('azure-function create', 'datafactory_linked_service_azure_function_create')
        g.generic_update_command('azure-function update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_linked_service_azure_function_update')
        g.custom_command('azure-key-vault create', 'datafactory_linked_service_azure_key_vault_create')
        g.generic_update_command('azure-key-vault update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_linked_service_azure_key_vault_update')
        g.custom_command('azure-m-l create', 'datafactory_linked_service_azure_m_l_create')
        g.generic_update_command('azure-m-l update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_azure_m_l_update')
        g.custom_command('azure-m-l-service create', 'datafactory_linked_service_azure_m_l_service_create')
        g.generic_update_command('azure-m-l-service update', setter_arg_name = 'properties', custom_func_name = 'datafa'
                                 'ctory_linked_service_azure_m_l_service_update')
        g.custom_command('azure-maria-d-b create', 'datafactory_linked_service_azure_maria_d_b_create')
        g.generic_update_command('azure-maria-d-b update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_linked_service_azure_maria_d_b_update')
        g.custom_command('azure-my-sql create', 'datafactory_linked_service_azure_my_sql_create')
        g.generic_update_command('azure-my-sql update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_azure_my_sql_update')
        g.custom_command('azure-postgre-sql create', 'datafactory_linked_service_azure_postgre_sql_create')
        g.generic_update_command('azure-postgre-sql update', setter_arg_name = 'properties', custom_func_name = 'datafa'
                                 'ctory_linked_service_azure_postgre_sql_update')
        g.custom_command('azure-search create', 'datafactory_linked_service_azure_search_create')
        g.generic_update_command('azure-search update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_azure_search_update')
        g.custom_command('azure-sql-d-w create', 'datafactory_linked_service_azure_sql_d_w_create')
        g.generic_update_command('azure-sql-d-w update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_linked_service_azure_sql_d_w_update')
        g.custom_command('azure-sql-database create', 'datafactory_linked_service_azure_sql_database_create')
        g.generic_update_command('azure-sql-database update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_linked_service_azure_sql_database_update')
        g.custom_command('azure-sql-m-i create', 'datafactory_linked_service_azure_sql_m_i_create')
        g.generic_update_command('azure-sql-m-i update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_linked_service_azure_sql_m_i_update')
        g.custom_command('azure-storage create', 'datafactory_linked_service_azure_storage_create')
        g.generic_update_command('azure-storage update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_linked_service_azure_storage_update')
        g.custom_command('azure-table-storage create', 'datafactory_linked_service_azure_table_storage_create')
        g.generic_update_command('azure-table-storage update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_linked_service_azure_table_storage_update')
        g.custom_command('cassandra create', 'datafactory_linked_service_cassandra_create')
        g.generic_update_command('cassandra update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_cassandra_update')
        g.custom_command('common-data-service-for-apps create', 'datafactory_linked_service_common_data_service_for_app'
                         's_create')
        g.generic_update_command('common-data-service-for-apps update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_linked_service_common_data_service_for_apps_update')
        g.custom_command('concur create', 'datafactory_linked_service_concur_create')
        g.generic_update_command('concur update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_concur_update')
        g.custom_command('cosmos-db create', 'datafactory_linked_service_cosmos_db_create')
        g.generic_update_command('cosmos-db update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_cosmos_db_update')
        g.custom_command('cosmos-db-mongo-db-api create', 'datafactory_linked_service_cosmos_db_mongo_db_api_create')
        g.generic_update_command('cosmos-db-mongo-db-api update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_linked_service_cosmos_db_mongo_db_api_update')
        g.custom_command('couchbase create', 'datafactory_linked_service_couchbase_create')
        g.generic_update_command('couchbase update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_couchbase_update')
        g.custom_command('custom-data-source create', 'datafactory_linked_service_custom_data_source_create')
        g.generic_update_command('custom-data-source update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_linked_service_custom_data_source_update')
        g.custom_command('db2 create', 'datafactory_linked_service_db2_create')
        g.generic_update_command('db2 update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_s'
                                 'ervice_db2_update')
        g.custom_command('drill create', 'datafactory_linked_service_drill_create')
        g.generic_update_command('drill update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked'
                                 '_service_drill_update')
        g.custom_command('dynamics create', 'datafactory_linked_service_dynamics_create')
        g.generic_update_command('dynamics update', setter_arg_name = 'properties', custom_func_name = 'datafactory_lin'
                                 'ked_service_dynamics_update')
        g.custom_command('dynamics-a-x create', 'datafactory_linked_service_dynamics_a_x_create')
        g.generic_update_command('dynamics-a-x update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_dynamics_a_x_update')
        g.custom_command('dynamics-crm create', 'datafactory_linked_service_dynamics_crm_create')
        g.generic_update_command('dynamics-crm update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_dynamics_crm_update')
        g.custom_command('eloqua create', 'datafactory_linked_service_eloqua_create')
        g.generic_update_command('eloqua update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_eloqua_update')
        g.custom_command('file-server create', 'datafactory_linked_service_file_server_create')
        g.generic_update_command('file-server update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_file_server_update')
        g.custom_command('ftp-server create', 'datafactory_linked_service_ftp_server_create')
        g.generic_update_command('ftp-server update', setter_arg_name = 'properties', custom_func_name = 'datafactory_l'
                                 'inked_service_ftp_server_update')
        g.custom_command('google-ad-words create', 'datafactory_linked_service_google_ad_words_create')
        g.generic_update_command('google-ad-words update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_linked_service_google_ad_words_update')
        g.custom_command('google-big-query create', 'datafactory_linked_service_google_big_query_create')
        g.generic_update_command('google-big-query update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_linked_service_google_big_query_update')
        g.custom_command('google-cloud-storage create', 'datafactory_linked_service_google_cloud_storage_create')
        g.generic_update_command('google-cloud-storage update', setter_arg_name = 'properties', custom_func_name = 'dat'
                                 'afactory_linked_service_google_cloud_storage_update')
        g.custom_command('greenplum create', 'datafactory_linked_service_greenplum_create')
        g.generic_update_command('greenplum update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_greenplum_update')
        g.custom_command('h-base create', 'datafactory_linked_service_h_base_create')
        g.generic_update_command('h-base update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_h_base_update')
        g.custom_command('h-d-insight create', 'datafactory_linked_service_h_d_insight_create')
        g.generic_update_command('h-d-insight update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_h_d_insight_update')
        g.custom_command('h-d-insight-on-demand create', 'datafactory_linked_service_h_d_insight_on_demand_create')
        g.generic_update_command('h-d-insight-on-demand update', setter_arg_name = 'properties', custom_func_name = 'da'
                                 'tafactory_linked_service_h_d_insight_on_demand_update')
        g.custom_command('hdfs create', 'datafactory_linked_service_hdfs_create')
        g.generic_update_command('hdfs update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_hdfs_update')
        g.custom_command('hive create', 'datafactory_linked_service_hive_create')
        g.generic_update_command('hive update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_hive_update')
        g.custom_command('http-server create', 'datafactory_linked_service_http_server_create')
        g.generic_update_command('http-server update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_http_server_update')
        g.custom_command('hubspot create', 'datafactory_linked_service_hubspot_create')
        g.generic_update_command('hubspot update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_hubspot_update')
        g.custom_command('impala create', 'datafactory_linked_service_impala_create')
        g.generic_update_command('impala update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_impala_update')
        g.custom_command('informix create', 'datafactory_linked_service_informix_create')
        g.generic_update_command('informix update', setter_arg_name = 'properties', custom_func_name = 'datafactory_lin'
                                 'ked_service_informix_update')
        g.custom_command('jira create', 'datafactory_linked_service_jira_create')
        g.generic_update_command('jira update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_jira_update')
        g.custom_command('magento create', 'datafactory_linked_service_magento_create')
        g.generic_update_command('magento update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_magento_update')
        g.custom_command('maria-d-b create', 'datafactory_linked_service_maria_d_b_create')
        g.generic_update_command('maria-d-b update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_maria_d_b_update')
        g.custom_command('marketo create', 'datafactory_linked_service_marketo_create')
        g.generic_update_command('marketo update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_marketo_update')
        g.custom_command('microsoft-access create', 'datafactory_linked_service_microsoft_access_create')
        g.generic_update_command('microsoft-access update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_linked_service_microsoft_access_update')
        g.custom_command('mongo-db create', 'datafactory_linked_service_mongo_db_create')
        g.generic_update_command('mongo-db update', setter_arg_name = 'properties', custom_func_name = 'datafactory_lin'
                                 'ked_service_mongo_db_update')
        g.custom_command('mongo-db-v2 create', 'datafactory_linked_service_mongo_db_v2_create')
        g.generic_update_command('mongo-db-v2 update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_mongo_db_v2_update')
        g.custom_command('my-sql create', 'datafactory_linked_service_my_sql_create')
        g.generic_update_command('my-sql update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_my_sql_update')
        g.custom_command('netezza create', 'datafactory_linked_service_netezza_create')
        g.generic_update_command('netezza update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_netezza_update')
        g.custom_command('o-data create', 'datafactory_linked_service_o_data_create')
        g.generic_update_command('o-data update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_o_data_update')
        g.custom_command('odbc create', 'datafactory_linked_service_odbc_create')
        g.generic_update_command('odbc update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_odbc_update')
        g.custom_command('office365 create', 'datafactory_linked_service_office365_create')
        g.generic_update_command('office365 update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_office365_update')
        g.custom_command('oracle create', 'datafactory_linked_service_oracle_create')
        g.generic_update_command('oracle update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_oracle_update')
        g.custom_command('oracle-service-cloud create', 'datafactory_linked_service_oracle_service_cloud_create')
        g.generic_update_command('oracle-service-cloud update', setter_arg_name = 'properties', custom_func_name = 'dat'
                                 'afactory_linked_service_oracle_service_cloud_update')
        g.custom_command('paypal create', 'datafactory_linked_service_paypal_create')
        g.generic_update_command('paypal update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_paypal_update')
        g.custom_command('phoenix create', 'datafactory_linked_service_phoenix_create')
        g.generic_update_command('phoenix update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_phoenix_update')
        g.custom_command('postgre-sql create', 'datafactory_linked_service_postgre_sql_create')
        g.generic_update_command('postgre-sql update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_postgre_sql_update')
        g.custom_command('presto create', 'datafactory_linked_service_presto_create')
        g.generic_update_command('presto update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_presto_update')
        g.custom_command('quick-books create', 'datafactory_linked_service_quick_books_create')
        g.generic_update_command('quick-books update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_quick_books_update')
        g.custom_command('responsys create', 'datafactory_linked_service_responsys_create')
        g.generic_update_command('responsys update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_responsys_update')
        g.custom_command('rest-service create', 'datafactory_linked_service_rest_service_create')
        g.generic_update_command('rest-service update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_rest_service_update')
        g.custom_command('salesforce create', 'datafactory_linked_service_salesforce_create')
        g.generic_update_command('salesforce update', setter_arg_name = 'properties', custom_func_name = 'datafactory_l'
                                 'inked_service_salesforce_update')
        g.custom_command('salesforce-marketing-cloud create', 'datafactory_linked_service_salesforce_marketing_cloud_cr'
                         'eate')
        g.generic_update_command('salesforce-marketing-cloud update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_linked_service_salesforce_marketing_cloud_update')
        g.custom_command('salesforce-service-cloud create', 'datafactory_linked_service_salesforce_service_cloud_create'
                         '')
        g.generic_update_command('salesforce-service-cloud update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_linked_service_salesforce_service_cloud_update')
        g.custom_command('sap-b-w create', 'datafactory_linked_service_sap_b_w_create')
        g.generic_update_command('sap-b-w update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_sap_b_w_update')
        g.custom_command('sap-cloud-for-customer create', 'datafactory_linked_service_sap_cloud_for_customer_create')
        g.generic_update_command('sap-cloud-for-customer update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_linked_service_sap_cloud_for_customer_update')
        g.custom_command('sap-ecc create', 'datafactory_linked_service_sap_ecc_create')
        g.generic_update_command('sap-ecc update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_sap_ecc_update')
        g.custom_command('sap-hana create', 'datafactory_linked_service_sap_hana_create')
        g.generic_update_command('sap-hana update', setter_arg_name = 'properties', custom_func_name = 'datafactory_lin'
                                 'ked_service_sap_hana_update')
        g.custom_command('sap-open-hub create', 'datafactory_linked_service_sap_open_hub_create')
        g.generic_update_command('sap-open-hub update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_linked_service_sap_open_hub_update')
        g.custom_command('sap-table create', 'datafactory_linked_service_sap_table_create')
        g.generic_update_command('sap-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_sap_table_update')
        g.custom_command('service-now create', 'datafactory_linked_service_service_now_create')
        g.generic_update_command('service-now update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'linked_service_service_now_update')
        g.custom_command('sftp create', 'datafactory_linked_service_sftp_create')
        g.generic_update_command('sftp update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_sftp_update')
        g.custom_command('shopify create', 'datafactory_linked_service_shopify_create')
        g.generic_update_command('shopify update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_shopify_update')
        g.custom_command('snowflake create', 'datafactory_linked_service_snowflake_create')
        g.generic_update_command('snowflake update', setter_arg_name = 'properties', custom_func_name = 'datafactory_li'
                                 'nked_service_snowflake_update')
        g.custom_command('spark create', 'datafactory_linked_service_spark_create')
        g.generic_update_command('spark update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked'
                                 '_service_spark_update')
        g.custom_command('sql-server create', 'datafactory_linked_service_sql_server_create')
        g.generic_update_command('sql-server update', setter_arg_name = 'properties', custom_func_name = 'datafactory_l'
                                 'inked_service_sql_server_update')
        g.custom_command('square create', 'datafactory_linked_service_square_create')
        g.generic_update_command('square update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_square_update')
        g.custom_command('sybase create', 'datafactory_linked_service_sybase_create')
        g.generic_update_command('sybase update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linke'
                                 'd_service_sybase_update')
        g.custom_command('teradata create', 'datafactory_linked_service_teradata_create')
        g.generic_update_command('teradata update', setter_arg_name = 'properties', custom_func_name = 'datafactory_lin'
                                 'ked_service_teradata_update')
        g.custom_command('vertica create', 'datafactory_linked_service_vertica_create')
        g.generic_update_command('vertica update', setter_arg_name = 'properties', custom_func_name = 'datafactory_link'
                                 'ed_service_vertica_update')
        g.custom_command('web create', 'datafactory_linked_service_web_create')
        g.generic_update_command('web update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_s'
                                 'ervice_web_update')
        g.custom_command('xero create', 'datafactory_linked_service_xero_create')
        g.generic_update_command('xero update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_xero_update')
        g.custom_command('zoho create', 'datafactory_linked_service_zoho_create')
        g.generic_update_command('zoho update', setter_arg_name = 'properties', custom_func_name = 'datafactory_linked_'
                                 'service_zoho_update')
        g.custom_command('delete', 'datafactory_linked_service_delete')

    from azext_datafactory.generated._client_factory import cf_dataset
    datafactory_dataset = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._dataset_operations#DatasetOperations.{'
        '}',
        client_factory=cf_dataset)
    with self.command_group('datafactory dataset', datafactory_dataset, client_factory=cf_dataset) as g:
        g.custom_command('list', 'datafactory_dataset_list')
        g.custom_show_command('show', 'datafactory_dataset_show')
        g.custom_command('amazon-m-w-s-object create', 'datafactory_dataset_amazon_m_w_s_object_create')
        g.generic_update_command('amazon-m-w-s-object update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_amazon_m_w_s_object_update')
        g.custom_command('amazon-redshift-table create', 'datafactory_dataset_amazon_redshift_table_create')
        g.generic_update_command('amazon-redshift-table update', setter_arg_name = 'properties', custom_func_name = 'da'
                                 'tafactory_dataset_amazon_redshift_table_update')
        g.custom_command('amazon-s3-object create', 'datafactory_dataset_amazon_s3_object_create')
        g.generic_update_command('amazon-s3-object update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_dataset_amazon_s3_object_update')
        g.custom_command('avro create', 'datafactory_dataset_avro_create')
        g.generic_update_command('avro update', setter_arg_name = 'properties', custom_func_name = 'datafactory_dataset'
                                 '_avro_update')
        g.custom_command('azure-blob create', 'datafactory_dataset_azure_blob_create')
        g.generic_update_command('azure-blob update', setter_arg_name = 'properties', custom_func_name = 'datafactory_d'
                                 'ataset_azure_blob_update')
        g.custom_command('azure-blob-f-s-file create', 'datafactory_dataset_azure_blob_f_s_file_create')
        g.generic_update_command('azure-blob-f-s-file update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_azure_blob_f_s_file_update')
        g.custom_command('azure-data-explorer-table create', 'datafactory_dataset_azure_data_explorer_table_create')
        g.generic_update_command('azure-data-explorer-table update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_azure_data_explorer_table_update')
        g.custom_command('azure-data-lake-store-file create', 'datafactory_dataset_azure_data_lake_store_file_create')
        g.generic_update_command('azure-data-lake-store-file update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_azure_data_lake_store_file_update')
        g.custom_command('azure-maria-d-b-table create', 'datafactory_dataset_azure_maria_d_b_table_create')
        g.generic_update_command('azure-maria-d-b-table update', setter_arg_name = 'properties', custom_func_name = 'da'
                                 'tafactory_dataset_azure_maria_d_b_table_update')
        g.custom_command('azure-my-sql-table create', 'datafactory_dataset_azure_my_sql_table_create')
        g.generic_update_command('azure-my-sql-table update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_azure_my_sql_table_update')
        g.custom_command('azure-postgre-sql-table create', 'datafactory_dataset_azure_postgre_sql_table_create')
        g.generic_update_command('azure-postgre-sql-table update', setter_arg_name = 'properties', custom_func_name = 
                                 'datafactory_dataset_azure_postgre_sql_table_update')
        g.custom_command('azure-search-index create', 'datafactory_dataset_azure_search_index_create')
        g.generic_update_command('azure-search-index update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_azure_search_index_update')
        g.custom_command('azure-sql-d-w-table create', 'datafactory_dataset_azure_sql_d_w_table_create')
        g.generic_update_command('azure-sql-d-w-table update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_azure_sql_d_w_table_update')
        g.custom_command('azure-sql-m-i-table create', 'datafactory_dataset_azure_sql_m_i_table_create')
        g.generic_update_command('azure-sql-m-i-table update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_azure_sql_m_i_table_update')
        g.custom_command('azure-sql-table create', 'datafactory_dataset_azure_sql_table_create')
        g.generic_update_command('azure-sql-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_azure_sql_table_update')
        g.custom_command('azure-table create', 'datafactory_dataset_azure_table_create')
        g.generic_update_command('azure-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_azure_table_update')
        g.custom_command('binary create', 'datafactory_dataset_binary_create')
        g.generic_update_command('binary update', setter_arg_name = 'properties', custom_func_name = 'datafactory_datas'
                                 'et_binary_update')
        g.custom_command('cassandra-table create', 'datafactory_dataset_cassandra_table_create')
        g.generic_update_command('cassandra-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_cassandra_table_update')
        g.custom_command('common-data-service-for-apps-entity create', 'datafactory_dataset_common_data_service_for_app'
                         's_entity_create')
        g.generic_update_command('common-data-service-for-apps-entity update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_common_data_service_for_apps_entity_update')
        g.custom_command('concur-object create', 'datafactory_dataset_concur_object_create')
        g.generic_update_command('concur-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_concur_object_update')
        g.custom_command('cosmos-db-mongo-db-api-collection create', 'datafactory_dataset_cosmos_db_mongo_db_api_collec'
                         'tion_create')
        g.generic_update_command('cosmos-db-mongo-db-api-collection update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_cosmos_db_mongo_db_api_collection_update')
        g.custom_command('cosmos-db-sql-api-collection create', 'datafactory_dataset_cosmos_db_sql_api_collection_creat'
                         'e')
        g.generic_update_command('cosmos-db-sql-api-collection update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_cosmos_db_sql_api_collection_update')
        g.custom_command('couchbase-table create', 'datafactory_dataset_couchbase_table_create')
        g.generic_update_command('couchbase-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_couchbase_table_update')
        g.custom_command('custom-dataset create', 'datafactory_dataset_custom_dataset_create')
        g.generic_update_command('custom-dataset update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_custom_dataset_update')
        g.custom_command('db2-table create', 'datafactory_dataset_db2_table_create')
        g.generic_update_command('db2-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_da'
                                 'taset_db2_table_update')
        g.custom_command('delimited-text create', 'datafactory_dataset_delimited_text_create')
        g.generic_update_command('delimited-text update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_delimited_text_update')
        g.custom_command('document-db-collection create', 'datafactory_dataset_document_db_collection_create')
        g.generic_update_command('document-db-collection update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_dataset_document_db_collection_update')
        g.custom_command('drill-table create', 'datafactory_dataset_drill_table_create')
        g.generic_update_command('drill-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_drill_table_update')
        g.custom_command('dynamics-a-x-resource create', 'datafactory_dataset_dynamics_a_x_resource_create')
        g.generic_update_command('dynamics-a-x-resource update', setter_arg_name = 'properties', custom_func_name = 'da'
                                 'tafactory_dataset_dynamics_a_x_resource_update')
        g.custom_command('dynamics-crm-entity create', 'datafactory_dataset_dynamics_crm_entity_create')
        g.generic_update_command('dynamics-crm-entity update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_dynamics_crm_entity_update')
        g.custom_command('dynamics-entity create', 'datafactory_dataset_dynamics_entity_create')
        g.generic_update_command('dynamics-entity update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_dynamics_entity_update')
        g.custom_command('eloqua-object create', 'datafactory_dataset_eloqua_object_create')
        g.generic_update_command('eloqua-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_eloqua_object_update')
        g.custom_command('file-share create', 'datafactory_dataset_file_share_create')
        g.generic_update_command('file-share update', setter_arg_name = 'properties', custom_func_name = 'datafactory_d'
                                 'ataset_file_share_update')
        g.custom_command('google-ad-words-object create', 'datafactory_dataset_google_ad_words_object_create')
        g.generic_update_command('google-ad-words-object update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_dataset_google_ad_words_object_update')
        g.custom_command('google-big-query-object create', 'datafactory_dataset_google_big_query_object_create')
        g.generic_update_command('google-big-query-object update', setter_arg_name = 'properties', custom_func_name = 
                                 'datafactory_dataset_google_big_query_object_update')
        g.custom_command('greenplum-table create', 'datafactory_dataset_greenplum_table_create')
        g.generic_update_command('greenplum-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_greenplum_table_update')
        g.custom_command('h-base-object create', 'datafactory_dataset_h_base_object_create')
        g.generic_update_command('h-base-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_h_base_object_update')
        g.custom_command('hive-object create', 'datafactory_dataset_hive_object_create')
        g.generic_update_command('hive-object update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_hive_object_update')
        g.custom_command('http-file create', 'datafactory_dataset_http_file_create')
        g.generic_update_command('http-file update', setter_arg_name = 'properties', custom_func_name = 'datafactory_da'
                                 'taset_http_file_update')
        g.custom_command('hubspot-object create', 'datafactory_dataset_hubspot_object_create')
        g.generic_update_command('hubspot-object update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_hubspot_object_update')
        g.custom_command('impala-object create', 'datafactory_dataset_impala_object_create')
        g.generic_update_command('impala-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_impala_object_update')
        g.custom_command('informix-table create', 'datafactory_dataset_informix_table_create')
        g.generic_update_command('informix-table update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_informix_table_update')
        g.custom_command('jira-object create', 'datafactory_dataset_jira_object_create')
        g.generic_update_command('jira-object update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_jira_object_update')
        g.custom_command('json create', 'datafactory_dataset_json_create')
        g.generic_update_command('json update', setter_arg_name = 'properties', custom_func_name = 'datafactory_dataset'
                                 '_json_update')
        g.custom_command('magento-object create', 'datafactory_dataset_magento_object_create')
        g.generic_update_command('magento-object update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_magento_object_update')
        g.custom_command('maria-d-b-table create', 'datafactory_dataset_maria_d_b_table_create')
        g.generic_update_command('maria-d-b-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_maria_d_b_table_update')
        g.custom_command('marketo-object create', 'datafactory_dataset_marketo_object_create')
        g.generic_update_command('marketo-object update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_marketo_object_update')
        g.custom_command('microsoft-access-table create', 'datafactory_dataset_microsoft_access_table_create')
        g.generic_update_command('microsoft-access-table update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_dataset_microsoft_access_table_update')
        g.custom_command('mongo-db-collection create', 'datafactory_dataset_mongo_db_collection_create')
        g.generic_update_command('mongo-db-collection update', setter_arg_name = 'properties', custom_func_name = 'data'
                                 'factory_dataset_mongo_db_collection_update')
        g.custom_command('mongo-db-v2-collection create', 'datafactory_dataset_mongo_db_v2_collection_create')
        g.generic_update_command('mongo-db-v2-collection update', setter_arg_name = 'properties', custom_func_name = 'd'
                                 'atafactory_dataset_mongo_db_v2_collection_update')
        g.custom_command('my-sql-table create', 'datafactory_dataset_my_sql_table_create')
        g.generic_update_command('my-sql-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_dataset_my_sql_table_update')
        g.custom_command('netezza-table create', 'datafactory_dataset_netezza_table_create')
        g.generic_update_command('netezza-table update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_netezza_table_update')
        g.custom_command('o-data-resource create', 'datafactory_dataset_o_data_resource_create')
        g.generic_update_command('o-data-resource update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_o_data_resource_update')
        g.custom_command('odbc-table create', 'datafactory_dataset_odbc_table_create')
        g.generic_update_command('odbc-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_d'
                                 'ataset_odbc_table_update')
        g.custom_command('office365-table create', 'datafactory_dataset_office365_table_create')
        g.generic_update_command('office365-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_office365_table_update')
        g.custom_command('oracle-service-cloud-object create',
                         'datafactory_dataset_oracle_service_cloud_object_create')
        g.generic_update_command('oracle-service-cloud-object update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_oracle_service_cloud_object_update')
        g.custom_command('oracle-table create', 'datafactory_dataset_oracle_table_create')
        g.generic_update_command('oracle-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_dataset_oracle_table_update')
        g.custom_command('orc create', 'datafactory_dataset_orc_create')
        g.generic_update_command('orc update', setter_arg_name = 'properties', custom_func_name = 'datafactory_dataset_'
                                 'orc_update')
        g.custom_command('parquet create', 'datafactory_dataset_parquet_create')
        g.generic_update_command('parquet update', setter_arg_name = 'properties', custom_func_name = 'datafactory_data'
                                 'set_parquet_update')
        g.custom_command('paypal-object create', 'datafactory_dataset_paypal_object_create')
        g.generic_update_command('paypal-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_paypal_object_update')
        g.custom_command('phoenix-object create', 'datafactory_dataset_phoenix_object_create')
        g.generic_update_command('phoenix-object update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_phoenix_object_update')
        g.custom_command('postgre-sql-table create', 'datafactory_dataset_postgre_sql_table_create')
        g.generic_update_command('postgre-sql-table update', setter_arg_name = 'properties', custom_func_name = 'datafa'
                                 'ctory_dataset_postgre_sql_table_update')
        g.custom_command('presto-object create', 'datafactory_dataset_presto_object_create')
        g.generic_update_command('presto-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_presto_object_update')
        g.custom_command('quick-books-object create', 'datafactory_dataset_quick_books_object_create')
        g.generic_update_command('quick-books-object update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_quick_books_object_update')
        g.custom_command('relational-table create', 'datafactory_dataset_relational_table_create')
        g.generic_update_command('relational-table update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_dataset_relational_table_update')
        g.custom_command('responsys-object create', 'datafactory_dataset_responsys_object_create')
        g.generic_update_command('responsys-object update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_dataset_responsys_object_update')
        g.custom_command('rest-resource create', 'datafactory_dataset_rest_resource_create')
        g.generic_update_command('rest-resource update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_rest_resource_update')
        g.custom_command('salesforce-marketing-cloud-object create', 'datafactory_dataset_salesforce_marketing_cloud_ob'
                         'ject_create')
        g.generic_update_command('salesforce-marketing-cloud-object update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_salesforce_marketing_cloud_object_update')
        g.custom_command('salesforce-object create', 'datafactory_dataset_salesforce_object_create')
        g.generic_update_command('salesforce-object update', setter_arg_name = 'properties', custom_func_name = 'datafa'
                                 'ctory_dataset_salesforce_object_update')
        g.custom_command('salesforce-service-cloud-object create', 'datafactory_dataset_salesforce_service_cloud_object'
                         '_create')
        g.generic_update_command('salesforce-service-cloud-object update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_salesforce_service_cloud_object_update')
        g.custom_command('sap-bw-cube create', 'datafactory_dataset_sap_bw_cube_create')
        g.generic_update_command('sap-bw-cube update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_sap_bw_cube_update')
        g.custom_command('sap-cloud-for-customer-resource create', 'datafactory_dataset_sap_cloud_for_customer_resource'
                         '_create')
        g.generic_update_command('sap-cloud-for-customer-resource update', setter_arg_name = 'properties',
                                 custom_func_name = 'datafactory_dataset_sap_cloud_for_customer_resource_update')
        g.custom_command('sap-ecc-resource create', 'datafactory_dataset_sap_ecc_resource_create')
        g.generic_update_command('sap-ecc-resource update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_dataset_sap_ecc_resource_update')
        g.custom_command('sap-hana-table create', 'datafactory_dataset_sap_hana_table_create')
        g.generic_update_command('sap-hana-table update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_sap_hana_table_update')
        g.custom_command('sap-open-hub-table create', 'datafactory_dataset_sap_open_hub_table_create')
        g.generic_update_command('sap-open-hub-table update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_sap_open_hub_table_update')
        g.custom_command('sap-table-resource create', 'datafactory_dataset_sap_table_resource_create')
        g.generic_update_command('sap-table-resource update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_sap_table_resource_update')
        g.custom_command('service-now-object create', 'datafactory_dataset_service_now_object_create')
        g.generic_update_command('service-now-object update', setter_arg_name = 'properties', custom_func_name = 'dataf'
                                 'actory_dataset_service_now_object_update')
        g.custom_command('shopify-object create', 'datafactory_dataset_shopify_object_create')
        g.generic_update_command('shopify-object update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_shopify_object_update')
        g.custom_command('snowflake-table create', 'datafactory_dataset_snowflake_table_create')
        g.generic_update_command('snowflake-table update', setter_arg_name = 'properties', custom_func_name = 'datafact'
                                 'ory_dataset_snowflake_table_update')
        g.custom_command('spark-object create', 'datafactory_dataset_spark_object_create')
        g.generic_update_command('spark-object update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_dataset_spark_object_update')
        g.custom_command('sql-server-table create', 'datafactory_dataset_sql_server_table_create')
        g.generic_update_command('sql-server-table update', setter_arg_name = 'properties', custom_func_name = 'datafac'
                                 'tory_dataset_sql_server_table_update')
        g.custom_command('square-object create', 'datafactory_dataset_square_object_create')
        g.generic_update_command('square-object update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_square_object_update')
        g.custom_command('sybase-table create', 'datafactory_dataset_sybase_table_create')
        g.generic_update_command('sybase-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory'
                                 '_dataset_sybase_table_update')
        g.custom_command('teradata-table create', 'datafactory_dataset_teradata_table_create')
        g.generic_update_command('teradata-table update', setter_arg_name = 'properties', custom_func_name = 'datafacto'
                                 'ry_dataset_teradata_table_update')
        g.custom_command('vertica-table create', 'datafactory_dataset_vertica_table_create')
        g.generic_update_command('vertica-table update', setter_arg_name = 'properties', custom_func_name = 'datafactor'
                                 'y_dataset_vertica_table_update')
        g.custom_command('web-table create', 'datafactory_dataset_web_table_create')
        g.generic_update_command('web-table update', setter_arg_name = 'properties', custom_func_name = 'datafactory_da'
                                 'taset_web_table_update')
        g.custom_command('xero-object create', 'datafactory_dataset_xero_object_create')
        g.generic_update_command('xero-object update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_xero_object_update')
        g.custom_command('zoho-object create', 'datafactory_dataset_zoho_object_create')
        g.generic_update_command('zoho-object update', setter_arg_name = 'properties', custom_func_name = 'datafactory_'
                                 'dataset_zoho_object_update')
        g.custom_command('delete', 'datafactory_dataset_delete')

    from azext_datafactory.generated._client_factory import cf_pipeline
    datafactory_pipeline = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._pipeline_operations#PipelineOperations'
        '.{}',
        client_factory=cf_pipeline)
    with self.command_group('datafactory pipeline', datafactory_pipeline, client_factory=cf_pipeline) as g:
        g.custom_command('list', 'datafactory_pipeline_list')
        g.custom_show_command('show', 'datafactory_pipeline_show')
        g.custom_command('create', 'datafactory_pipeline_create')
        g.generic_update_command('update', setter_arg_name = 'pipeline', custom_func_name = 'datafactory_pipeline_updat'
                                 'e')
        g.custom_command('delete', 'datafactory_pipeline_delete')
        g.custom_command('create-run', 'datafactory_pipeline_create_run')

    from azext_datafactory.generated._client_factory import cf_pipeline_run
    datafactory_pipeline_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._pipeline_run_operations#PipelineRunOpe'
        'rations.{}',
        client_factory=cf_pipeline_run)
    with self.command_group('datafactory pipeline-run', datafactory_pipeline_run,
                            client_factory=cf_pipeline_run) as g:
        g.custom_show_command('show', 'datafactory_pipeline_run_show')
        g.custom_command('cancel', 'datafactory_pipeline_run_cancel')
        g.custom_command('query-by-factory', 'datafactory_pipeline_run_query_by_factory')

    from azext_datafactory.generated._client_factory import cf_activity_run
    datafactory_activity_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._activity_run_operations#ActivityRunOpe'
        'rations.{}',
        client_factory=cf_activity_run)
    with self.command_group('datafactory activity-run', datafactory_activity_run,
                            client_factory=cf_activity_run) as g:
        g.custom_command('query-by-pipeline-run', 'datafactory_activity_run_query_by_pipeline_run')

    from azext_datafactory.generated._client_factory import cf_trigger
    datafactory_trigger = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._trigger_operations#TriggerOperations.{'
        '}',
        client_factory=cf_trigger)
    with self.command_group('datafactory trigger', datafactory_trigger, client_factory=cf_trigger) as g:
        g.custom_command('list', 'datafactory_trigger_list')
        g.custom_show_command('show', 'datafactory_trigger_show')
        g.custom_command('create', 'datafactory_trigger_create')
        g.generic_update_command('update', setter_arg_name = 'properties', custom_func_name = 'datafactory_trigger_upda'
                                 'te')
        g.custom_command('delete', 'datafactory_trigger_delete')
        g.custom_command('get-event-subscription-status', 'datafactory_trigger_get_event_subscription_status')
        g.custom_command('query-by-factory', 'datafactory_trigger_query_by_factory')
        g.custom_command('start', 'datafactory_trigger_start', supports_no_wait=True)
        g.custom_command('stop', 'datafactory_trigger_stop', supports_no_wait=True)
        g.custom_command('subscribe-to-event', 'datafactory_trigger_subscribe_to_event', supports_no_wait=True)
        g.custom_command('unsubscribe-from-event', 'datafactory_trigger_unsubscribe_from_event',
                         supports_no_wait=True)
        g.wait_command('wait')

    from azext_datafactory.generated._client_factory import cf_trigger_run
    datafactory_trigger_run = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._trigger_run_operations#TriggerRunOpera'
        'tions.{}',
        client_factory=cf_trigger_run)
    with self.command_group('datafactory trigger-run', datafactory_trigger_run, client_factory=cf_trigger_run) as g:
        g.custom_command('query-by-factory', 'datafactory_trigger_run_query_by_factory')
        g.custom_command('rerun', 'datafactory_trigger_run_rerun')

    from azext_datafactory.generated._client_factory import cf_data_flow
    datafactory_data_flow = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._data_flow_operations#DataFlowOperation'
        's.{}',
        client_factory=cf_data_flow)
    with self.command_group('datafactory data-flow', datafactory_data_flow, client_factory=cf_data_flow) as g:
        g.custom_command('list', 'datafactory_data_flow_list')
        g.custom_show_command('show', 'datafactory_data_flow_show')
        g.custom_command('create', 'datafactory_data_flow_create')
        g.generic_update_command('update', setter_arg_name = 'properties', custom_func_name = 'datafactory_data_flow_up'
                                 'date')
        g.custom_command('delete', 'datafactory_data_flow_delete')

    from azext_datafactory.generated._client_factory import cf_data_flow_debug_session
    datafactory_data_flow_debug_session = CliCommandType(
        operations_tmpl='azext_datafactory.vendored_sdks.datafactory.operations._data_flow_debug_session_operations#Dat'
        'aFlowDebugSessionOperations.{}',
        client_factory=cf_data_flow_debug_session)
    with self.command_group('datafactory data-flow-debug-session', datafactory_data_flow_debug_session,
                            client_factory=cf_data_flow_debug_session) as g:
        g.custom_command('create', 'datafactory_data_flow_debug_session_create', supports_no_wait=True)
        g.custom_command('delete', 'datafactory_data_flow_debug_session_delete')
        g.custom_command('add-data-flow', 'datafactory_data_flow_debug_session_add_data_flow')
        g.custom_command('execute-command', 'datafactory_data_flow_debug_session_execute_command',
                         supports_no_wait=True)
        g.custom_command('query-by-factory', 'datafactory_data_flow_debug_session_query_by_factory')
        g.wait_command('wait')
