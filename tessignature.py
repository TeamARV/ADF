import oci

# Especificar la ubicación del archivo de configuración
config_path = "C:\\my_oci_config\\config"

# Crear una configuración predeterminada usando el archivo de configuración personalizado
config = oci.config.from_file(config_path)

# Inicializar el cliente de Object Storage con la configuración personalizada
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Parámetros necesarios para listar los objetos
namespace_name = "ocuocictrng3"
bucket_name = "bucketPrivado"

# Listar los objetos en el bucket (opcional)
list_objects_response = object_storage_client.list_objects(
    namespace_name=namespace_name,
    bucket_name=bucket_name,
)

# Obtener las credenciales necesarias del archivo de configuración
tenancy = config["tenancy"]
user = config["user"]
fingerprint = config["fingerprint"]
private_key = config["key_file"]

# Crear un RequestSigner usando las credenciales
signer = oci.auth.signers.get_resource_principals_signer()

# Construir la URL para listar objetos (o cualquier otra operación)
url = f"https://objectstorage.{config['region']}.oraclecloud.com/n/{namespace_name}/b/{bucket_name}/o"

# Firmar la URL
signed_url = signer.sign_uri(url, oci.signer.RequestSigner.SIGNER_TYPE_RESOURCE_PRINCIPAL)

# Imprimir la URL firmada
print(f"Signed URL: {signed_url}")
