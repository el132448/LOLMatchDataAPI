import package

def main():
    # get setting from database
    setting = ["大涼粉",'tw2','SEA',100,450,'RGAPI-d0df3f5e-06ee-4b76-ac3c-a2c93d3651aa',
                      "gfh2NBRvQfamzlVNBVKT7V7AV_4N5aBiPWQODvOvAkkNF6zVbr1D0cmKlWd2uOr5sNGYYGdu80G8-Q",
                      1623801600,int(package.time.time())]

    # instantiate Object
    player = package.Setting(setting[0],setting[1],setting[2],setting[3],setting[4],setting[5],
                      setting[6],setting[7],setting[8])

    # choose mode
    player.chooseMode()
    
if __name__ == '__main__':
    main()
#===================================================================
#===================================================================
# NOTE future improvement
# input -> create instance
# run method
#===================================================================
#=================================================================== 
# NOTE
# RATE LIMITS
# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)
# queue type:  https://static.developer.riotgames.com/docs/lol/queues.json (450: 5v5 ARAM games)
# print(match_data) is unprintable due to: UnicodeEncodeError: 'cp950' codec can't encode character '\u56fd' in position 42806: illegal multibyte sequence
# TW2 is SEA
# df.to_csv("output.csv")
#
# *****VERY IMPORTANT: PUUID IS BASED ON API_KEY, USE NAME TO UPDATE PUUID
# {
#     "id": "q_VbiXGSaTUX5poczFzHlx-4BDuEMDTL0eYZ9z0DYFvcPofIUAUE4SLSUA",
#     "accountId": "kHHxJKaBALnaHq9tD_WfCsfPK2-rUDNyQ8fOujVJmtn5PH_vUod4Pfbi",
#     "puuid": "_O3-HqbZnECzfLYJp6_HfzFRyDTmxXX34ZM8E_iXsiJI4AKqJJuvenjzoQJfUS3MQe4yu25goY0xVQ",
#     "name": "大涼粉",
#     "profileIconId": 4618,
#     "revisionDate": 1701099556937,
#     "summonerLevel": 367
# }

# {
#     "id": "a6tOeGtr1RFzZOmPR2BLOKShNJRZr_n8XOHlqkJbYj5xBvgJjUXMwj4kgQ",
#     "accountId": "t7GnjsSQ88gtMNCjJujdwlSBfh4mXX3w1eLP2iv8mb2teX3GuhwSYBiy",
#     "puuid": "syzv8DpgDAOV8tncJnP78wfeU7XXvfj6AJzyA2r8xXBJ3M-D4lHSKmmDh4NkRPUp5fDUPI1xtEYy3A",
#     "name": "國士無雙十三面聽",
#     "profileIconId": 3163,
#     "revisionDate": 1702138722995,
#     "summonerLevel": 424
# }

# {
#     "id": "OFtEwiARKMdmvgX12uvfWMIHc8-fIBQkBKhgHU_Ot3NnrQdIJSf0_rv7pA",
#     "accountId": "3tsEpxJRC2k2PofZ2VHpORaadJq2C9XekymmqGHZYRBtCEURDo7crAJr",
#     "puuid": "bDaB4b0IcEVc4aetZLuTZK5eGvGxUtDhanCgqF7As1lt1mlR2hgk2kjwyJZAjke7xaoqUpTQnlGLOA",
#     "name": "笨蛋變態吵死了",
#     "profileIconId": 5417,
#     "revisionDate": 1702136498926,
#     "summonerLevel": 499
# }

# {
#     "id": "bdIXeTp6zefqcmBqLGbR7elL3lYt7JTM2eM0IIfkMrb-SqlDmyXddhbkmw",
#     "accountId": "SgjLGa7aOt1Rji5StILGAmKJ-ZuKNsqpvz3gJi9PfQz73lswHayhBTjO",
#     "puuid": "toPG93O9EkeGLawesa8i7snxlEKwNLmJb6wlpdTX2u7WddUo7SYvpXu0eZmJxjkRMTtcE_ecorqZsQ",
#     "name": "全Loss 35P",
#     "profileIconId": 3182,
#     "revisionDate": 1702136498926,
#     "summonerLevel": 564
# }

# {
#     "id": "NpCk33njn2ByCVHtsxEt2kF9GpPEJtYLrn1oO6ay4CgXDaTF20aez6x3lw",
#     "accountId": "QwAoCuAp4uJGvKpSZvQoP4FIDd5je9tYf_FkZVo1XKSc2Y-ZxWIWFlUH",
#     "puuid": "wr-aWYpChIybwAhfGiUU--7M-mELbO44EjveDD-tE0zZ83dBD9um5Dq2OXQi5Fv8j9hf83Bv3aW-1A",
#     "name": "OnewaySubaru486",
#     "profileIconId": 1211,
#     "revisionDate": 1702151525075,
#     "summonerLevel": 395
# }

# {
#     "id": "ylT7NYN3zMiQfqfbcqPFQt6YlLjF6S67-FP3gE6W2P8xPQxcvALHzbMONQ",
#     "accountId": "gzhnlPSgx0Ru8g-xx_-mfWfXTA930-VzBF4CCm_zDiAM4sD2k7ISRzBq",
#     "puuid": "cCNDq9RiEunEXOXVLaZpHNK7-dNZ8KjzAfPEpsv91vZJqGqYNrZgqL6qr_0VfrSoMOUHsYbgmQOWWQ",
#     "name": "滑她咩墮",
#     "profileIconId": 4353,
#     "revisionDate": 1702049275000,
#     "summonerLevel": 381
# }

# {
#     "id": "3ajoaDpFvkYNzjJnsnqSQ6mmri0s6U2KG0iatBTfkyjrw67MjbwNTHgjUg",
#     "accountId": "UUm7Nkl64srtmQYp5Ssx6GjKC5hNojmHBDYBrv5_hrEcumLzNDqO9Is4",
#     "puuid": "Byk-hUyyb2c_5FvkQcnbty-H5dp-0o3fqhrHV83Z_qJohORSg86YswB2x5WXMN5wUW2_-iUHkTrKFg",
#     "name": "下北澤奇跡大天使",
#     "profileIconId": 5413,
#     "revisionDate": 1701934238000,
#     "summonerLevel": 217
# }

# [ Setup for testing
#   total 14 games 
#     "TW2_3693774", "gameStartTimestamp": 1673796800182, 20230120
#     "TW2_3684593",
#     "TW2_3212099",
#     "TW2_3196388",
#     "TW2_3170661",
#     "TW2_2792493",
#     "TW2_2095254",
#     "TW2_1239465",
#     "TW2_1230672",
#     "TW2_894293",
#     "TW2_602623",
#     "TW2_590810",
#     "TW2_585259",
#     "TW2_566690"   # this is the last game readable
# ]

# https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/_O3-HqbZnECzfLYJp6_HfzFRyDTmxXX34ZM8E_iXsiJI4AKqJJuvenjzoQJfUS3MQe4yu25goY0xVQ/ids?startTime=1623801600&endTime=1701557401&queue=450&start=0&count=10&api_key=RGAPI-e0f2217d-1843-4789-8ec0-0a4c74b62ba5
# https://sea.api.riotgames.com/lol/match/v5/matches/by-puuid/_O3-HqbZnECzfLYJp6_HfzFRyDTmxXX34ZM8E_iXsiJI4AKqJJuvenjzoQJfUS3MQe4yu25goY0xVQ/ids?startTime=1623801600&endTime=1701557401&queue=450&start=0&count=10&api_key=RGAPI-43a702b6-6d78-4c72-80d2-7e25a92fc7fd