from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import os
from read_data import read_feminist_data, find_matching_feminist

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
        feminist_data = read_feminist_data()
        matching_feminist = find_matching_feminist(birthday, feminist_data)
        
        if matching_feminist:
            response = {
                "name": matching_feminist["名字"],
                "motto": matching_feminist["金句"],
                "representative_work": matching_feminist["代表作"],
                "mbti": matching_feminist["MBTI"],
                "introduction": matching_feminist["人物介绍小传"],
                "avatar": f"/avatars/Beauvoir_avator.jpeg"  # 假设头像文件名与名字相同
            }
        else:
            response = {
                "message": "未找到匹配的角色模型。",
                "status": "error"
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
