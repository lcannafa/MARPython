import dropbox
from dropbox.files import WriteMode #SI ALGO FALLA, COMENTAR ESTA LINEA

# subir_archivo
# Requiere:
# - reporte: archivo docx para subir a Dropbox


def subir_archivo(reporte):
    dbx = dropbox.Dropbox('8M2rk1A9ebAAAAAAAAAACqdQetGZhLSBSeh8mCjOo4_JOrs251ya-bRZcGlBZWXV') # Clave de la API de Dropbox
    with open(reporte, 'rb') as f:
        dbx.files_upload(f.read(), '/Reportes/' + reporte, mode=dropbox.files.WriteMode.overwrite) #SI ALGO FALLA, BORRAR A PARTIR DE "mode"
        link = dbx.files_get_temporary_link('/Reportes/' + reporte)

    return link
