import oci

# Especificar la ubicación del archivo de configuración
config_path = "C:\\my_oci_config\\config"

# Crear una configuración predeterminada usando el archivo de configuración personalizado
config = oci.config.from_file(config_path)

# Inicializar el cliente de Object Storage con el archivo de configuración personalizado
object_storage_client = oci.object_storage.ObjectStorageClient(config)

# Parámetros necesarios para la descarga del archivo
namespace_name = "ocuocictrng3"
bucket_name = "bucketPrivado"
object_name = "file_fscmtopmodelam_scmextractam_doobiccextractam_fulfilllineextractpvo-batch1232618921-20240708_202141.zip"
file_path = "D:\\file.zip"  # Ruta local donde se guardará el archivo descargado



try:
    # Descargar el objeto desde Object Storage
    response = object_storage_client.get_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name
    )

    # Guardar el contenido del archivo en disco
    with open(file_path, 'wb') as f:
        for chunk in response.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)

    print(f"Archivo descargado exitosamente a: {file_path}")

except oci.exceptions.ServiceError as e:
    print(f"Error al descargar el archivo: {e}")