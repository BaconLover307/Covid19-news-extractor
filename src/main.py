from Form import Form

form = Form('coba.txt', 'terkonfirmasi positif', 'optionBM')
form.readFile()
for ans in form.info:
    print(ans)