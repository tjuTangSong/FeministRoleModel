from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)  # 在这里应用 CORS，确保在任何路由之前

# 假设你的图片存储在项目根目录的 'avatars' 文件夹中
AVATAR_FOLDER = 'avatars'

@app.route('/match_role_model', methods=['POST'])
def process_input():
    data = request.json
    birthday = data.get('birthday')
    book = data.get('book')

    try:
        birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        age = (datetime.datetime.now() - birthday_date).days // 365
        
        if age < 30 and "科技" in book:
            name = "谢尔盖·布林"
            motto = "不作恶。"
            avatar_file = "Beauvoir_avator.jpeg"
        elif age >= 30 and "文学" in book:
            name = "西蒙娜·德·波伏瓦"
            motto = "人不是生而为女人的，而是成为女人的。"
            avatar_file = "Beauvoir_avator.jpeg"
        else:
            name = "玛丽·居里"
            motto = "在生活中，没有什么可怕的，只有应该了解的。"
            avatar_file = "Beauvoir_avator.jpeg"
        
        # 构建图片的URL
        avatar_url = f"/avatars/{avatar_file}"
        
        response = {
            "name": name,
            "motto": motto,
            "avatar": avatar_url
        }
    except ValueError:
        response = {
            "message": "生日格式不正确，请使用 YYYY-MM-DD 格式。",
            "status": "error"
        }

    return jsonify(response)

# 添加一个路由来提供图片文件
@app.route('/avatars/<filename>')
def serve_avatar(filename):
    return send_from_directory(AVATAR_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)

