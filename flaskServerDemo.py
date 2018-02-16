import serial
from flask import Flask, request
app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 0)

@app.route('/drive/', methods=['GET'])
def default():
    ikeys = ['LV','LH','RV', 'RH']
    values = ['0','0','0','0']
    if request.method == 'GET':
        for x in range(0, 4):
            values[x] = request.args.get(ikeys[x])
            ser.write(values[x].encode())
            ser.write(',')
        ser.write('T')

        for x in range(0,4):
            print(values[x])

        line = ser.readline()
        print(line)
        return line

@app.route('/status/', methods=['GET'])
def status():
    line = ser.readline()
    print(line)
    #return 'true'
    return line

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)

