from polylabel import polylabel
import pyautogui
a = [[884.0, 440.0], [886.0, 424.0], [886.0, 419.0], [886.0, 419.0], [886.0, 415.0], [886.0, 415.0], [886.0, 408.0], [885.0, 404.0], [881.0, 404.0], [881.0, 392.0], [874.0, 392.0], [874.0, 388.0], [873.0, 388.0], [873.0, 375.0], [873.0, 375.0], [873.0, 373.0], [869.0, 373.0], [869.0, 355.0], [869.0, 355.0], [869.0, 345.0], [869.0, 345.0], [869.0, 344.0], [866.0, 344.0], [866.0, 334.0], [866.0, 334.0], [866.0, 332.0], [867.0, 332.0], [867.0, 329.0], [867.0, 329.0], [867.0, 306.0], [853.0, 306.0], [853.0, 305.0], [831.0, 305.0], [831.0, 299.0], [826.0, 299.0], [826.0, 287.0], [824.0, 287.0], [824.0, 275.0], [806.0, 275.0], [806.0, 298.0], [732.0, 298.0], [732.0, 300.0], [728.0, 300.0], [728.0, 299.0], [722.0, 299.0], [722.0, 296.0], [684.0, 296.0], [684.0, 309.0], [684.0, 309.0], [684.0, 312.0], [710.0, 312.0], [710.0, 316.0], [695.0, 316.0], [695.0, 313.0], [660.0, 313.0], [666.0, 340.0], [728.0, 340.0], [728.0, 339.0], [729.0, 339.0], [729.0, 336.0], [745.0, 336.0], [745.0, 334.0], [745.0, 334.0], [745.0, 324.0], [814.0, 324.0], [814.0, 339.0], [814.0, 339.0], [814.0, 340.0], [835.0, 340.0], [835.0, 348.0], [836.0, 348.0], [836.0, 351.0], [838.0, 351.0], [838.0, 358.0], [841.0, 358.0], [841.0, 366.0], [841.0, 366.0], [841.0, 368.0], [843.0, 368.0], [843.0, 370.0], [847.0, 370.0], [847.0, 372.0], [847.0, 372.0], [847.0, 373.0], [846.0, 373.0], [846.0, 389.0], [846.0, 389.0], [846.0, 394.0], [842.0, 394.0], [842.0, 406.0], [842.0, 406.0], [842.0, 409.0], [837.0, 409.0], [837.0, 430.0], [837.0, 430.0], [837.0, 437.0], [844.0, 437.0], [844.0, 440.0]]

res = polylabel([a])
pyautogui.moveTo(int(res[0]), int(res[1]))
