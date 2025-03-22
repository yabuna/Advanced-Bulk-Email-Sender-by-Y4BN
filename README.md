<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Y4BN - Bulk Email Sender</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Orbitron', sans-serif;
        }

        body {
            background-color: #030f0f;
            color: #00df82;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .container {
            background: rgba(3, 98, 76, 0.2);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0, 223, 130, 0.6);
            max-width: 500px;
        }

        h1 {
            font-size: 28px;
            color: #00df82;
        }

        .tagline {
            font-size: 18px;
            margin-bottom: 10px;
            color: #ffffffb3;
        }

        .info p {
            font-size: 16px;
            color: #ffffffb3;
            margin-bottom: 15px;
        }

        .y4bn {
            font-weight: bold;
            color: #00df82;
        }

        .btn {
            display: inline-block;
            margin: 10px;
            padding: 12px 20px;
            font-size: 16px;
            color: #030f0f;
            background: #00df82;
            border: none;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .btn:hover {
            background: #03a06b;
            transform: scale(1.05);
        }

        .secondary {
            background: transparent;
            border: 2px solid #00df82;
            color: #00df82;
        }

        .secondary:hover {
            background: #00df82;
            color: #030f0f;
        }

        .footer {
            margin-top: 15px;
            font-size: 14px;
            color: #ffffffb3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ Bulk Email Sender</h1>
        <p class="tagline">Fast. Secure. Powerful.</p>
        
        <div class="info">
            <p>Welcome to the most efficient **Bulk Email Sender** designed by <span class="y4bn">Y4BN</span>.</p>
            <p>Easily send bulk emails using multiple SMTP servers, with real-time **Telegram notifications**.</p>
        </div>
        
        <a href="https://github.com/Y4BN/BulkEmailSender" target="_blank" class="btn">📂 View on GitHub</a>
        <a href="https://t.me/Y4BN" target="_blank" class="btn secondary">💬 Contact on Telegram</a>
        
        <div class="footer">
            <p>🚀 Developed by <span class="y4bn">Y4BN</span> | Stay Anonymous, Stay Safe.</p>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const tagline = document.querySelector(".tagline");
            const words = ["Fast.", "Secure.", "Powerful."];
            let index = 0;
            let charIndex = 0;
            let isDeleting = false;

            function typeEffect() {
                let currentWord = words[index];
                if (isDeleting) {
                    tagline.textContent = currentWord.substring(0, charIndex--);
                } else {
                    tagline.textContent = currentWord.substring(0, charIndex++);
                }

                if (!isDeleting && charIndex === currentWord.length) {
                    isDeleting = true;
                    setTimeout(typeEffect, 1500);
                } else if (isDeleting && charIndex === 0) {
                    isDeleting = false;
                    index = (index + 1) % words.length;
                }
                setTimeout(typeEffect, isDeleting ? 50 : 100);
            }

            typeEffect();
        });
    </script>
</body>
</html>
