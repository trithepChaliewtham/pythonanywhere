with open('studen.csv','r') as f :
    for line in f.readlines():

        a = line.strip().split('\t')

        sid,name,email,nick = a[0], a[1], a[2] ,a[3]


        std_template = {
            "model" : "blog.student",
            "pk": {sid},
            "field": {
                "name": {name}
                "email": {email}
                "nick": {nick}


                }
        },\n'




            }