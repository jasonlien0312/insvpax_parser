# inspvax parser
##### This program takes in inspvax data and outputs csv files. The form of inspvax data should be the following:
<pre>
header:  
id: 1465  
  msg_type: 0  
  port_addr: 160  
  length: 126  
  sequence: 0  
...  
azimuth_std: 0.118529580534  
extended_status: 184553671  
seconds_since_update: 0  
</pre>
##### The csv file consists of a header row and data rows. Ecah row represents a single inspvax data. 
