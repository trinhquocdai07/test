import json
import requests
import aiohttp
import asyncio
import time
from datetime import datetime, timedelta, timezone

# Configuration (use environment variables or a config file in production)
SDT = "0989489307"
PW = "Trinhdai2442007@"
TOKEN_BOT = "7854045615:AAE2GSximfpkX4Mf8rJue1aeXR1Sxa-1N28"
UID_TELE = "6652727298"

# Headers for API requests
HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://id.hsa.edu.vn',
    'Referer': 'https://id.hsa.edu.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'X-Recaptcha-Token': '03AFcWeA4XTL_1bohvqY13F7PwVtNTnwbs9tzAXI-HA1Bwla_Tvv4f-wUsTGm9J_V6kGSAx0m9m9dbND-iAW9btm2n-HcIVu237c-qIIxHIfB1DVHooEcFjhbAFsvESYqCh9stfuF6aqHl5nM3aKo-KLJu3923lFi6_3JpvXeAZbC3_OzZe1CfDUxtZnpEmjN1OPXgsgYmxDEUR4uvYEgh12waVM4revy-Y0Q2MyriMvxYIaofX0s4fXT3w3IyijGxRS6RXFFFA2L-_U-qH_qoV5SdHT1PVwmuqV0eKOV5sSuRS22x0MR-fO5ZCjOmC1Q1zf_RWdB4RslUlVRhD0RHNMRDrNcr8tMPmpFOU_ksFVrMj_ySRBIyrXPMoVAk9vt1UcY0qFogofjQYPTN4IUhw1fFWfJhkVgmcBuuJ5wi4XFyB0WvQb7Rxg4p8i8UvqyHLHsei00M-hh0u-ZquxxePLDsk2MmxzGC4eAjJj7Sam9DzipZzQhO4IdGzB1yDHjhNLKDRx13nD7AHDS8toprYnIHlIiK6Ue_nK8-tuQyRosW0rlrha_tqlkC5dMV_MDuFb8SUwK6K1Rq1Y8RzZb3J_HkHdMMFmUCo1BaRhU5y6af_oRdJbN9gG8Bzxmu8PxwYN_c4OSpQvojliewM7op1N8kW9LeeeCC-rS9JJbAihxwyki-e93WUzgDCXX428C54RSmzvmCgjfDRk7M8gtH6Kx5XQXDndAgaZgNf6mU47fAK3L8VN9NVppSi48KJl7Wt6BOXxZjJZpiUd6hB1nN7bYZwSV8sHgPqjJylF6FtxryWnP_yk16tB4HVGuqbAOkZxjodXWowz0aPg-IVEUwDWsdMcS99ZDjy9YHA0yro_JtDYNwi6yyyY17f5sj2iHDJbUTRK8WsFgnM3fh6An8nwX9Wi0qXyfbk2YcYy51_Q76MzPfgds_Chd7ZMrWHpQzvlLzpE147d31G0yHfCCe54Trh3MECrhhP1WZyI_Kki5ShjEqcyiTGlGWL0gSWIUi_JiCVoF0SlrVkpnL8FX-0ACVpdjoRoqREqr5UzkcwWXf23qBv2NfQ905Pe8Euh4sSp8PzLj73gRzL26vb4vpOOXIu9R55YIe-jUK1TETZjMAjfSoysV5bt7BTWCm-mToCAcX7IjR67ywIVAoCc7K_Pb-Lsw9PiIv_JiKvk83QfznWVBaaukZsJNgL-ykgujBwT_XmlHQkt8YPVT1kXTpEBzGFJJpoTy2ZzxzPcbTpae89ddj0dxhU4F-W-ReZnVrVsDbqOmqMOx6IJhiGGd5OmVe-TMCOB8PTmO1dvU-IQRUYrfCryjsT1voepDJgszF6SWR6aGIga20iX4Hu6h_II_GqAsyDGaXiQe5vW1B3q9Ym0yIas6f4JsXpfpyMTlnAHu6vm3yCLFCPe7kHi30o0lFyiVeNLo3k7LV1FczEeu8wg_l0xHL-yF5lDakGnWXEdwnlkJKgEMEkhu5jL74CD35C5UdEAvxb8hj0AEzpeTokBjH8OUlWbVZIWspzUr9IiXHQfQPBe6LH9_KZfQ8TS8PZDLuWHZnGLcg8zOykRZJwLwR1g87ee4yORBdew3oUfuMxfYWtAdUtxOjNUYtUpkthyTCqSka804Ws5fSHSN1htR6Auh1VOnD2G5AyPRd2rC6FdVTmq8DUC7nqQ8b_Tpv0lAkW3rdlevwRwyP171qqJECw-060cOf9k0RXrR5uRjcMCo5csRcsPN69M7X2cnvaIo7ek4o_L4o3xFSDNXZbaVHsOjya3gpBq3hppqe886Y_Y8xV_yLWKciAvkHF1ZCc9XR282LLfhLAqVI7mb5PhA_ncHM9KsfZU1bXErzKsXyg1VU3HeNfvHdqQJ2iAUWsbyvrrHnOdTyuL9H39rQb8S1QdIqmv7Y7uI-QulIN1F7bS-JAyYgtpo303cuSQgrFPQgGAmx0Ex5Jf32Z2n54gSVkqLjo9TQARSG1dqFYPKJ5YNnxYpbTN-oCuMtgxWYmhWdZ_1b3-YRQ4HKdSEbXY3_OM9LY6rZPBTf2ayVY8Vf1193tMa4q3l1qw5Y3N1LrHZ8xdXO1CXn-vPgCs4hBMEjwgkhwFU',  # Add your token here
    'save-data': 'on',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

async def send_telegram_message(text, chat_id, token):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            return await response.json()

def login(sdt, pw):
    json_data = {'id': sdt, 'password': pw}
    response = requests.post('https://api.hsa.edu.vn/accounts/sign-in', headers=HEADERS, json=json_data)
    response.raise_for_status()
    token = response.json()["token"]
    print("Token từ API đăng nhập:", token)
    return token

def get_exam_periods(headers):
    response = requests.get('https://api.hsa.edu.vn/exam/views/registration/available-period', headers=headers)
    response.raise_for_status()
    periods = response.json()
    print("Danh sách kỳ thi:", json.dumps(periods, indent=4, ensure_ascii=False))
    return periods

def get_locations(period_id, headers):
    params = {'batchId': period_id}
    response = requests.get('https://api.hsa.edu.vn/exam/views/registration/available-location', params=params, headers=headers)
    response.raise_for_status()
    locations = response.json()
    print("Danh sách địa điểm:", json.dumps(locations, indent=4, ensure_ascii=False))
    return locations

def get_batches(location_id, headers):
    params = {'periodId': location_id}
    response = requests.get('https://api.hsa.edu.vn/exam/views/registration/available-batch', params=params, headers=headers)
    response.raise_for_status()
    batches = response.json()
    print("Danh sách đợt thi:", json.dumps(batches, indent=4, ensure_ascii=False))
    return batches

def get_slots(batch_id, headers):
    params = {'locationId': batch_id}
    response = requests.get('https://api.hsa.edu.vn/exam/views/registration/available-slot', params=params, headers=headers)
    response.raise_for_status()
    slots = response.json()
    print("Danh sách ca thi:", json.dumps(slots, indent=4, ensure_ascii=False))
    return slots

def process_events(event_data):
    processed_events = []
    gmt7 = timezone(timedelta(hours=7))

    for event in event_data:
        event_time = datetime.fromisoformat(event["eventDateTime"].replace("Z", "+00:00"))
        event_time_gmt7 = event_time.astimezone(gmt7)
        formatted_time = event_time_gmt7.strftime("%d/%m/%Y - %H:%M")
        seat_status = "Hết chỗ" if int(event["registeredSlots"]) >= int(event["numberOfSeats"]) else "Còn chỗ"
        processed_events.append({
            "seatStatus": seat_status,
            "name": event["name"],
            "status": event["status"],
            "eventDateTime": formatted_time
        })
    print("Danh sách ca thi đã xử lý:", json.dumps(processed_events, indent=4, ensure_ascii=False))

    return processed_events

async def main():
    try:
        token = login(SDT, PW)
        headers = HEADERS.copy()
        headers['Authorization'] = f'Bearer {token}'

        periods = get_exam_periods(headers)
        for period in periods:
            batches = get_batches(period["id"], headers)
            for batch in batches:
                locations = get_locations(batch["id"], headers)
                for location in locations:
                    slots = get_slots(location["id"], headers)
                    processed_slots = process_events(slots)
                    for slot in processed_slots:
                        if slot["seatStatus"] == "Còn chỗ":
                            message = (f"Đợt: {batch['name']}\n"
                                      f"Đang trong vị trí còn trống:\n"
                                      f"Trường: {location['name']}\n"
                                      f"Địa chỉ: {location['address']['detail']}, {location['address']['ward']}, {location['address']['district']}\n"
                                      f"Ngày: {slot['eventDateTime']}")
                            await send_telegram_message(message, UID_TELE, TOKEN_BOT)
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    while True:
        asyncio.run(main())
        time.sleep(60)  # Sleep for 60 seconds to avoid rate limiting