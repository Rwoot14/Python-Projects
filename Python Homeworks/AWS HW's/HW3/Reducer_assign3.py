#!/usr/bin/python
import sys
# initiates the current email adress 
current_email=None
#opens a dictionary
dic={}
# loops through lines generated by mapper
for line in sys.stdin:
    # Gets rid of white space 
    if not line.strip():
        continue
    else:
        line=line.strip()
        # gets fields from mapper
        email,message_id=line.split('\t')
        # for all similar emails append the message id to the opend list
        if current_email==email:
            lis.append(message_id)
        else:
            if current_email:
                # assings the email to the list of message ids
                dic[email]=lis
                for i in dic:
                    print '%s\t%s' % (i,dic[i])
                    print '\n'
                #opens new empty dictionary
                dic={}
            # opens the list and appends the first message id and sets the first email
            lis=[]
            lis.append(message_id)
            current_email=email



