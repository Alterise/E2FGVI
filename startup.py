import subprocess


def process_video(video_path, mask_path, result_path , mp4_name="", is_linux=False):
    subprocess.run(["docker", "run", "--rm", "--gpus all" if is_linux else "--gpus=all",
                    "-v", video_path + ":/app/video_input",
                    "-v", mask_path + ":/app/mask_input",
                    "-v", result_path + ":/app/results", "-t", "alterise/video-inpainting",
                    "--model", "e2fgvi_hq", "--video", "video_input" + ("" if mp4_name == "" else ("/" + mp4_name)), "--mask", "mask_input",
                    "--ckpt", "release_model/E2FGVI-HQ-CVPR22.pth"])


# process_video("R:/GitHub/input/tennis", "R:/GitHub/input/tennis_mask", "R:/GitHub/results")
# process_video("R:/GitHub/input", "R:/GitHub/input/schoolgirls_mask", "R:/GitHub/results", "schoolgirls.mp4")
