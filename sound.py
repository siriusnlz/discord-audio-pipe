import sounddevice as sd
from pprint import pformat

DEFAULT = 0
sd.default.channels = 2
sd.default.dtype = 'float32'
sd.default.blocksize = 18000
sd.default.dither_off = True
sd.default.latency = 'high'
sd.default.clip_off = True
sd.default.samplerate = 48000


class PCMStream:
    def __init__(self):
        self.stream = None

    def read(self, num_bytes):
        # frame is 4 bytes
        frames = int(num_bytes / 4)
        data = self.stream.read(frames)[0]

        # convert to pcm format
        return bytes(data)

    def change_device(self, num):
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()

        self.stream = sd.RawInputStream(device=num, blocksize=18000)
        self.stream.start()


class DeviceNotFoundError(Exception):
    def __init__(self):
        self.devices = sd.query_devices()
        self.host_apis = sd.query_hostapis()
        super().__init__('No Devices Found')

    def __str__(self):
        return (
            f'Devices \n'
            f'{self.devices} \n '
            f'Host APIs \n'
            f'{pformat(self.host_apis)}'
        )


def query_devices():
    options = {
        device.get('name'): index
        for index, device in enumerate(sd.query_devices())
        if (device.get('max_input_channels') > 0 and
            device.get('hostapi') == DEFAULT)
    }

    if not options:
        raise DeviceNotFoundError()

    return options
