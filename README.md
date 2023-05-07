# TuneFlow Python Plugin Examples

## Requirements

Python >= 3.7

## Run the demo plugins

See https://help.tuneflow.com/en/developer/python-devguide.html#debug-your-plugin for more details on how to debug a plugin locally.

To run a demo plugin in TuneFlow:

1. `cd` to the root folder of the plugin

2. Install dependencies if there is any:

```bash
pip install -r requirements.txt
```

3. Run the debug host:

```bash
python debug.py
```

4. Start TuneFlow Desktop, create or open a song.

5. Open "TuneFlow Plugin Library" panel on the right side, and in the upper-right corner, click on "Load a local plugin in debug mode".
