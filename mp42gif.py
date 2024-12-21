from moviepy.editor import VideoFileClip
from PIL import Image
import os

def mp4_to_resized_gif(input_path, output_path, resize_factor=0.5, fps=10):
    # 打开视频文件
    clip = VideoFileClip(input_path)
    
    # 创建临时目录存放帧图片
    temp_folder = "temp_frames"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    # 读取视频帧并保存为图片
    frame_filenames = []
    for i, frame in enumerate(clip.iter_frames(fps=fps, dtype="uint8")):
        img = Image.fromarray(frame)
        resized_img = img.resize([int(resize_factor * s) for s in img.size])
        frame_filename = os.path.join(temp_folder, f"frame_{i:04d}.png")
        resized_img.save(frame_filename)
        frame_filenames.append(frame_filename)
        if i==20:
            break
    # 将所有帧组合成GIF
    images = [Image.open(f) for f in frame_filenames]
    images[0].save(output_path, save_all=True, append_images=images[1:], duration=1000/fps, loop=0)

    # 清理临时文件
    for f in frame_filenames:
        os.remove(f)
    os.rmdir(temp_folder)

# 设置输入输出路径和调整大小的比例
input_mp4 = "result/a4_output_v8_p2_noaug.mp4"  # 输入MP4文件路径
output_gif = "result/output.gif"  # 输出GIF文件路径
resize_factor = 0.2  # 缩放比例，可以根据需要调整
fps = 10  # 每秒帧数，可以根据需要调整

# 调用函数进行转换
mp4_to_resized_gif(input_mp4, output_gif, resize_factor, fps)