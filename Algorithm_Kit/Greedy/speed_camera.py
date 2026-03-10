def speed_camera(routes):
    answer = 1
    routes.sort(key=lambda x:(x[1], x[0]))
    camera = routes.pop(0)[1]

    while routes:
        if routes[0][0] > camera:
            camera = routes.pop(0)[1]
            answer += 1
        else:
            routes.pop(0)

    return answer




print(speed_camera([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # result = 2