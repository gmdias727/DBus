import time
from halo import Halo

spinner = Halo(
    color='blue',
    spinner='monkey',
    placement='right',
)

spinner.start(
    text='D-Bus service running >'
)
spinner.succeed(text='aqui rodou suave')

if(True == 1):
    spinner.fail('failed')
    spinner.stop()

time.sleep(3)
spinner.stop()