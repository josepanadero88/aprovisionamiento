import os

# En el Jenkinsfile haremos que el contenedor 'cliente' haga un curl
response = os.system("curl -s web-preproduccion:8083 | grep 'José Alfonso Panadero Estudillo'")

with open("result.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<testsuites>\n  <testsuite name="WebCheck">\n')
    if response == 0:
        f.write('    <testcase name="VerificarNombre" status="passed"/>\n')
    else:
        f.write('    <testcase name="VerificarNombre" status="failed">\n')
        f.write('      <failure message="Nombre no encontrado en la web"/>\n    </testcase>\n')
    f.write('  </testsuite>\n</testsuites>')

if response != 0:
    exit(1)
