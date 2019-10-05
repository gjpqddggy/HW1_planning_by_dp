import numpy as np
import matplotlib.pyplot as plt

envDir = 'environment/'
saveDir = 'results/'
filename = 'gridmap_4'

def valueEvaluation(m, p):
    nm = np.copy(m)
    for i in range(1, m.shape[0]-1):
        for j in range(1, m.shape[1]-1):
            if m[i][j] != 0.0:
                up = p[i][j][0]*(-1+m[i-1][j]) if m[i-1][j] != -100 else p[i][j][0]*(-1+m[i][j])
                down = p[i][j][1]*(-1+m[i+1][j]) if m[i+1][j] != -100 else p[i][j][1]*(-1+m[i][j])
                left = p[i][j][2]*(-1+m[i][j-1]) if m[i][j-1] != -100 else p[i][j][2]*(-1+m[i][j])
                right = p[i][j][3]*(-1+m[i][j+1]) if m[i][j+1] != -100 else p[i][j][3]*(-1+m[i][j])
                nm[i][j] = up + down + left + right
    return nm

def policyImprovement(m, p):
    newp = np.copy(p)
    for i in range(1, m.shape[0]-1):
        for j in range(1, m.shape[1]-1):
            if m[i][j] != 0.0:
                up = round(m[i-1][j] if m[i-1][j] != -100 else m[i][j], 6)
                down = round(m[i+1][j] if m[i+1][j] != -100 else m[i][j], 6)
                left = round(m[i][j-1] if m[i][j-1] != -100 else m[i][j], 6)
                right = round(m[i][j+1] if m[i][j+1] != -100 else m[i][j], 6)
                list = [up, down, left, right]
                list.sort(reverse=True)
                # print(list)
                cnt = 0
                for k in list:
                    cnt += 1 if list[0] == k else 0
                # print(cnt)
                newp[i][j][0] = 1/cnt if up == list[0] else 0
                newp[i][j][1] = 1/cnt if down == list[0] else 0
                newp[i][j][2] = 1/cnt if left == list[0] else 0
                newp[i][j][3] = 1/cnt if right == list[0] else 0
    return newp



def policyIteration(m, p):
    print('V1\n' + str(m))
    # print('P1\n' + str(p))
    idx = 2
    while 1:
        nm = valueEvaluation(m, p)
        newp = policyImprovement(nm, p)
        if np.array_equal(nm, m):
            break
        print('V' + str(idx) + '\n' + str(nm))
        # print('P' + str(idx) + '\n' + str(newp))
        m = nm
        p = newp
        idx += 1
    # print(newp)
    plot(newp, m, 'pi')


def valueIteration(m, p):
    print('V1\n' + str(m))
    index = 2
    while 1:
        nm = np.copy(m)
        for i in range(1, m.shape[0]-1):
            for j in range(1, m.shape[1]-1):
                if m[i][j] != 0.0:
                    nm[i][j] = -1 + max(m[i][j-1], m[i][j+1], m[i+1][j], m[i-1][j])

        if np.array_equal(nm, m):
            break
        print('V' + str(index) + '\n' + str(nm))
        m = nm
        index += 1
    newp = policyImprovement(nm,p)
    # print(newp)
    plot(newp, nm, 'vi')

def plot(policy, m, mode):
        # settings
        ax = plt.gca()
        ax.set_xlim(0, m.shape[1])
        ax.set_ylim(0, m.shape[0])
        miloc = plt.MultipleLocator(1)
        ax.xaxis.set_minor_locator(miloc)
        ax.yaxis.set_minor_locator(miloc)
        ax.grid(which='minor')

        # plot policy
        for i in range(1, m.shape[0]-1):
            for j in range(1, m.shape[1]-1):
                if policy[i][j][3] > 0: plt.arrow(j+0.5, (m.shape[0])-i-0.5, 0.3, 0, width=0.02)
                if policy[i][j][2] > 0: plt.arrow(j+0.5, (m.shape[0])-i-0.5, -0.3, 0, width=0.02)
                if policy[i][j][1] > 0: plt.arrow(j+0.5, (m.shape[0])-i-0.5, 0, -0.3, width=0.02)
                if policy[i][j][0] > 0: plt.arrow(j+0.5, (m.shape[0])-i-0.5, 0, 0.3, width=0.02)

        #plt.show()
        plt.savefig(saveDir + filename + '_' + mode + ".png")
        plt.close()

def generatePolicy(map):
    _shape = [map.shape[0], map.shape[1], 4]
    policy = np.ones(_shape)*0.25
    for i in range(1, map.shape[0]-1):
        for j in range(1, map.shape[1]-1):
            if map[i][j] == 0:
                policy[i][j][0] = 0.0
                policy[i][j][1] = 0.0
                policy[i][j][2] = 0.0
                policy[i][j][3] = 0.0
    return policy


if __name__ == '__main__':
    map = np.loadtxt(envDir + filename + '.txt')
    policy = generatePolicy(map)
    print('policy iteration')
    policyIteration(map, policy)
    print('value iteration')
    valueIteration(map, policy)
