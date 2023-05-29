function get_currnet_coordinate(callback) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                const lat = position.coords.latitude; // 위도
                const lon = position.coords.longitude; // 경도
                callback([lat, lon]); // 위치 정보를 콜백 함수로 전달
            },
            function (error) {
                callback(null); // 오류 발생 시 null을 콜백 함수로 전달
            }
        );
    } else {
        callback(null);
    }
}


// 주어진 위도와 경도 사이의 거리를 계산하는 함수
function calculateDistance(lat1, lon1, lat2, lon2) {
    var R = 6371; // 지구의 반지름 (단위: km)
    var dLat = (lat2 - lat1) * Math.PI / 180;
    var dLon = (lon2 - lon1) * Math.PI / 180;
    var a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var distance = R * c;

    return distance;
}


