class Installation:
    def __init__(self):
        self.cameras = []
        self.rolls_size = 300
        self.scraps = []

    def add_cameras(self):
        print("Enter the camera cable lenght:")
        camera_length = input().strip()
        print(
            f'How much cameras of the lenght {camera_length} you will need:'
        )
        camera_num = int(input().strip())
        for _ in range(camera_num):
            self.cameras.append(int(camera_length))

    def set_roll(self):
        print("Enter the roll size:")
        roll = int(input().strip())
        self.rolls_size = roll

    def get_list(self):
        return {
            "cameras": self.cameras,
            "rolls_size": self.rolls_size,
            "scraps": self.scraps
        }

    def organize_installation(self):
        cameras_avaliable = self.cameras
        cameras_avaliable.sort(reverse=True)
        rolls_used = {}
        roll_number = 1
        cam_number = 1

        while len(cameras_avaliable) >= cam_number:
            remaining_length = self.rolls_size
            rolls_used[roll_number] = []

            for i, camera in enumerate(cameras_avaliable):
                if i >= cam_number-1:
                    if camera <= remaining_length:
                        rolls_used[roll_number].append(
                            (cam_number, f'Camera de {camera} metros')
                        )
                        remaining_length -= camera
                        cam_number += 1

            if remaining_length > 0:
                rolls_used[roll_number].append(
                    ('scraps', f'Sobra de {remaining_length} metros')
                )
            else:
                rolls_used[roll_number].append(
                    ('scraps', 'Sem sobras')
                )

            roll_number += 1

        return rolls_used


install = Installation()
install.add_cameras()
print(install.get_list()["cameras"])
print(install.organize_installation())
