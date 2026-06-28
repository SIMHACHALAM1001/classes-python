records=dict()
records_2={
    "name":"arun",
    "college":"vasavi engineering"
}
google_object={
    "profile":[
        {
        "name":"simhachalam",
        "address":"hitech city"
        },
        {
         "name":"arun"
        },
        {
         "name":"adarsh"
        }
    ]
}

profile_data = google_object.get("profile",[])
for item in profile_data:
    user_name = item.get("name",'')
    user_address = item.get("address", None)
    if user_address is None:
        item["address"] = "Hyderabad"
        # item.update(address="Hyderabad")

# for item in google_object["profile"]:
    # print(item["name"]+","+item["address"])

# records_3={
#     "college":[{
#         "name":"vasavi engineering college",
#         "student_count":1000
#         "staff_memebers":[{
#             "name":"arun",
#             "subject":"mathematics"
#         },.....]
#     },{
#         "name":"CBIT engineering college"


#     },{
#         "name":"malla reddy engineering college"

#     }]

#

sample_data={
    "name":"arun",
    "address":[{
        "line1":"Flat no: 201",
        "line2":"Jntu",
        "line3":"Pincode: 500090, hyderbad , Telangana"
    }],
    "degree":"B-tech"
}
# print(sample_data.keys())
# print(sample_data.values())
# print(sample_data.items()) # dict_item([(key, value),(key, value)])

# for key, value in sample_data.items():
#     print(key, value)

data="simhachalhhhamhhh"
# result={
#     s:1
#     i:1
#     m:2
#     h:2
#     a:3
#     l:1
# }

# result["h"] = 1 # update
# result["h"]  # access
# loop & get single letter
# result={}
# result["s"] = 1 // result["h"] = 1  
# result["h"] = result["h"](1)+1
# 
result = {}
for letter in data:
    if result.get(letter): # result[letter]
       result[letter] = result[letter] + 1
    else:
        result[letter] = 1
print(result)









