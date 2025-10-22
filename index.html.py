<!DOCTYPE html>
<html>
<head>
    <title>AI/ML Object Detection + Tracking</title>
    <style>
        body { font-family: Arial; text-align: center; background-color: #f0f0f0; }
        h1 { color: #333; }
        #video-container { display: inline-block; margin-top: 20px; }
        #chat { margin-top: 20px; max-width: 600px; margin-left:auto; margin-right:auto; background:#fff; padding:10px; border-radius:10px; height:200px; overflow-y:auto; }
    </style>
</head>
<body>
    <h1>AI/ML Object Detection + Tracking</h1>
    <div id="video-container">
        <img src="{{ url_for('video_feed') }}" width="640" height="480">
    </div>
    <div id="chat">
        <p>Chat log will appear here...</p>
    </div>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
