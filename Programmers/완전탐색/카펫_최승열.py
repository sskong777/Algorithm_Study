
def solution(brown, yellow):
    def quad(b, c):
        return [int((-b+(b**2-4*c)**0.5)/2), int((-b-(b**2-4*c)**0.5)/2)]
    return quad(-((brown + 4) // 2), yellow + brown)

    # 해설
    
    # Brown의 개수는 가로*2 + 세로*2 - 4
    # brown = w * 2 + h * 2 - 4 
    
    # w, h에 대해 정리하면
    # w + h = (brown + 4) // 2 
    # 간략화를 위해 B = (brown + 4) // 2 -> w + h = B
    
    # 넓이는 brown + yellow
    # w * h = brown + yellow 
    
    # 정리한 뒤 h에 B-w 대입
    # h = B - w
    # w * (B - w) = yellow + brown
    # Bw - w^2 = yellow + brown
    
    # w에 대한 이차방정식 성립
    # w^2 - Bw + (yellow+brown) = 0

    # 근의 공식 사용
    # a = 1
    # b = -((brown + 4) // 2)
    # c = yellow + brown
    
    # x1 = (-b+(b**2-4*c)**0.5)/2
    # x2 = (-b-(b**2-4*c)**0.5)/2
    
    # x1 * x2 는 넓이이기에 x1이 width라면 x2는 height이다.
    
    