import board
import pulseio
import adafruit_irremote

# Create a pulse input on pin GP2 (or whichever pin you are using),
# with a max capture length of 120
pulsein = pulseio.PulseIn(board.GP2, maxlen=120, idle_state=True)

# Create a decoder (NEC by default)
decoder = adafruit_irremote.GenericDecode()

print("Ready to receive IR signals...")

while True:
    # read pulses
    pulses = decoder.read_pulses(pulsein)
    try:
        code = decoder.decode_bits(pulses)  # No 'debug' param
        print("IR code received:", code)
    except adafruit_irremote.IRNECRepeatException:
        print("IR code repeated!")
    except adafruit_irremote.IRDecodeException as e:
        print("Failed to decode:", e)

