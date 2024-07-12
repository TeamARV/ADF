#print("Hello, World!")

# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Especificar la ubicación del archivo de configuración
config_path = "C:\\my_oci_config\\config"

# Crear una configuración predeterminada usando el archivo de configuración personalizado
config = oci.config.from_file(config_path)

# Inicializar el cliente de Object Storage con el archivo de configuración personalizado
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Parámetros necesarios para listar los objetos
namespace_name = "ocuocictrng3"
bucket_name = "bucketPrivado"
#prefix = "your_prefix"  # Si deseas listar solo objetos con un prefijo específico

# Listar los objetos en el bucket
list_objects_response = object_storage_client.list_objects(
    namespace_name=namespace_name,
    bucket_name=bucket_name,
    #prefix=prefix
)



# Obtener los datos de la respuesta
print(list_objects_response.data)
