import pprint


class InstallationMajor:
    def __init__(self):
        self.cameras = [150, 150, 150, 90, 90, 150, 90, 150, 90]
        self.rolls_size = 300
        self.scraps = []
        self.organization = {}

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
        index_cameras = [
            (i, camera) for i, camera in enumerate(self.cameras)
        ]
        return pprint.pprint({
            "cameras": index_cameras,
            "rolls_size": self.rolls_size,
            "scraps": self.scraps,
            "organization": self.organization
        })

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
                self.scraps.append(remaining_length)
            else:
                rolls_used[roll_number].append(
                    ('scraps', 'Sem sobras')
                )

            roll_number += 1

        self.organization = rolls_used
        return rolls_used


install = InstallationMajor()
install.organize_installation()
install.get_list()
