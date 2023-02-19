# Playing audio on Xavier

use `sox` to play silence 

define a device in SOX [link](https://linux.debian.user.narkive.com/9UGarD0X/specifying-a-device-for-sox-output#:~:text=environment.%20e.g.-,%22AUDIODEV%3Dhw%3A0%2C0%20play%20foo.wav%22%20t,-o%20play%20on)

avoid "no default audio device configured" install for sox 14.4.2 [link](https://github.com/sreuter/node-speakable/issues/18#:~:text=Nov%2023%2C%202021-,In%20case%20someone%20else%20%E2%80%93%20here%20in%20the%20future%20%E2%80%93%20still%20gets%20stuck%20with%20this%20problem.%20For%20me%2C%20using%2014.4.2%2C%20the%20issue%20was%20fixed%20after%20installing%20SoX%20handlers%20for%20other%20audio%20formats.,-sudo%20apt%20install)


install a service to run silence in background [link](https://unix.stackexchange.com/questions/362223/short-audio-playback-is-muted-requires-warming-up-or-secondary-audio-in-backgro#:~:text=UPDATE%202-,Lazy%20as%20I%20am%2C%20I%20didn%27t%20report%20this%20to%20ALSA%20developers%2C%20yet%2C%20but%2C%20I%27ve%20create%20a%20user%20systemd%20unit%3A,-%5BUnit%5D%0ADescription%3DContinuous)

dmix alsa [link](https://alsa.opensrc.org/Dmix)