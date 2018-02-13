
#! reliable transport layer protocol transmittor 
""" no NAK
sender not contrained by TCP flow and congestion control
No fragmentation (data from above is less than MSS in size) """

nextSeqNum = initialSeqNum
sendBase = initialSeqNum

While True:
	# event: data received from application above
	if flag == true:
		segment = newTCP(nextSeqNum)
		# timer is currently running
		if timer == 0:
			# start timer
			startTimer()
		transfer_to_IP(segment)
		nextSeqNum = nextSeqNum + len(data)
		break

	# timeout event (global timer) timeout_period is set by AIMD algorithm
	if timer == timeout_period:
		for segment in notAcknowledgedSegements:
			transfer_to_IP(segment)
		startTimer()
		break

	# event: acknowledgement recieved
	if segment.ackNum > sendBase:
		sendBase = segment.ackNum
		if not notAcknowledgedSegements:
			startTimer()
	break
