import subprocess
import shutil

input_filename = 'Reporte 0.docx'
output_filename = 'output.pdf'

p = subprocess.Popen(['unoconv', '--stdout', input_filename], stdout=subprocess.PIPE)
with open(output_filename, 'w') as output:
   shutil.copyfileobj(p.stdout, output)