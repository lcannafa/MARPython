import dropbox

def subir_archivo(reporte):
    dbx = dropbox.Dropbox('8M2rk1A9ebAAAAAAAAAACqdQetGZhLSBSeh8mCjOo4_JOrs251ya-bRZcGlBZWXV')
    with open(reporte, 'rb') as f:
        var = 'nueva var para que actualice'
        dbx.files_upload(f.read(), '/Reportes/' + reporte)
        link = dbx.files_get_temporary_link('/Reportes/' + reporte)

    return link
