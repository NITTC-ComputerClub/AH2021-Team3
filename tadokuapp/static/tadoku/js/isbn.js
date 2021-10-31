function onScanSuccess(decodedText) {
    document.forms[0].elements["isbn"].value = decodedText;
    html5QrcodeScanner.clear();
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader", { fps: 10, qrbox: 250 });

html5QrcodeScanner.render(onScanSuccess);
