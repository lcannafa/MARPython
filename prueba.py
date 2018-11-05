import dropbox

dbx = dropbox.Dropbox('8M2rk1A9ebAAAAAAAAAACqdQetGZhLSBSeh8mCjOo4_JOrs251ya-bRZcGlBZWXV')
nombreArchivo = 'Reporte 49.docx'

path = '/machineAR/' + nombreArchivo
with open(nombreArchivo, errors='ignore') as f:
    k = f.read()
    print(k)
    dbx.files_upload(f.read(), path)