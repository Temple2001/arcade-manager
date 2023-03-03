const axios = require('axios');

const day = ['일', '월', '화', '수', '목', '금', '토'];

class ApiClient {
    constructor() {
        const client = axios.create({
            baseURL: 'http://localhost:5000',
        });
        client.interceptors.response.use((resp) => {
            return resp.data;
        });
        
        this.client = client;
    }

    // KST 변환 및 포맷 수정
    dateFormatter(date) {
        date = new Date(date);
        date.setHours(date.getHours() + 9);
        return date.getFullYear() + '년 ' + (date.getMonth() + 1) + '월 ' + date.getDate() + '일 ' + day[date.getDay()] + '요일 ' + date.getHours() + '시 ' + date.getMinutes() + '분 ' + date.getSeconds() + '초';
    }

    async getData() {
        const response = await this.client.get('log-data');
        for (let i = 0; i < response.length; i++) {
            let each = response[i];
            each.log_time = this.dateFormatter(each.log_time);
            
        }
        return response;
    }
}

async function main() {
    const api_client = new ApiClient();
    const res = await api_client.getData();
    console.log(res);
}

module.exports = ApiClient;