The sample data is in the file named TEST.txt. The data file will always be named TEST.txt.

***************************************************

Every line of data in TEST.txt has the same information. The format is:

Subject_ID, DateTime, x_accel, y_accel, z_accel, pitch, roll, orientation/

(Subject_ID, DateTime) is a primary identifier for the data.

DateTime format is Year-Month-Day Hour:Minute:Second, in format XXXX-XX-XX XX:XX:XX

pitch and roll are accurate to 3 decimal places.

***************************************************

The data is formated as above per-request of the client.

The pitch and roll are calculated using the x_accel, y_accel, and z_accel.
Orientation is calculated from pitch and roll. It is an enumerated value, which is defined as
{
  0 : prone,
  1 : inclined,
  2 : upright,
  3 : reclined,
  4 : supine,
}

x_accel, y_accel, and z_accel are occasionally refered to as sensorvalue0, sensorvalue1, and sensorvalue2, respectively.

