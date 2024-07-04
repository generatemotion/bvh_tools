import re
import json
from io import StringIO

import glm
import copy


import struct
 
def array_to_bytes(arr,t="i"):
    # 假设arr是一个整数列表
    return b''.join([struct.pack(t, num) for num in arr])


# define some structure 
class NodeData():
    def __init__(self):
        self.positionChannels = []
        self.rotationChannels = []
        self.positionData = []
        self.rotationData = []
    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ["positionChannels", "rotationChannels", "positionData", "rotationData"]

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

class HierarchyData():
    nodeDatas = []
    def __init__(self):
        self.nodeDatas = []
    
    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ["nodeDatas"]

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)


class FrameData():
    values = []
    def __init__(self):
        self.values = []

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ["values"]

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)


class MotionData():
    frames: int = 1
    frameTime: float = 0.0
    frameDatas = []
    def __init__(self):
        return
    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ["frames", "frameTime", "frameDatas"]

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

def trim(str):
    """
    remove all type of blank space
    """
    if str is None:
        return ""
    else:
        tmp = re.sub('\s|\t|\n', ' ', str)
        tmp = tmp.strip()
        tmp = " ".join(tmp.split())
        return tmp


class BvhTool():
    bvhContent = ""
    
    dictGLTF = {}
    hierarchyData = dict(HierarchyData())
    motionData = dict(MotionData())
    offset = 0
    byteData = b""
    nodeIndex = 0

    bvhFileName="Example1.bvh"
    saveGltfName="untitled.gltf"
    saveBinaryName="untitled.bin"

    
    

    def __init__(self):
        self.initGLTF()
        return 
    def initGLTF(self):
        dictGLTF = {
            "asset": {
                "version":"2.0"
            },
            "scenes": [{
                "nodes":[]
            }],
            "buffers": [{
                "uri":self.saveBinaryName
            }],
            "bufferViews": [{
                "buffer": 0
            }],
            "accessors":[{
                "componentType":5126,
                "type":"MAT4",
                "bufferView":0
            }],
            "skins": [{
                "joints": [],
                "inverseBindMatrices": 0
            }],
            "nodes": [],
            "animations": [{
                "samplers": [],
                "channels": []
            }],


        }
        self.dictGLTF = dictGLTF

    def loadFile(self,fileName):
        file = open(fileName, "r")
        try:
            text = file.read()
            # print(text)
            self.bvhContent = text
            return True
        
        finally:
            file.close()
    def saveFile(self, output, filename, t="wb"):
        file = open(filename, t)
        file.write(output)
        file.close()
        return True

    # this is a  recursive function
    def generateHierarchy( self, nodeIndex, parentMatrix ):
        """
        todo

        """
        # dictGLTF = self.dictGLTF
        # byteData = self.byteData
        # hierarchyData = self.hierarchyData
        # offset = self.offset
        # bvhLines = self.bvhLines

        currentMatrix = parentMatrix
        line = self.bvhLines[self.offset]
        tokens = trim(line).split(" ")
        print("generateHierarchy==>", self.offset)
        # return    

        while (self.offset < len(self.bvhLines)):
            line = self.bvhLines[self.offset]
            tokens = trim(line).split(" ")
            # if(line.rfind("ROOT", 0) == 0):
            print("tokens==>", tokens)
            if (tokens[0] == "ROOT"):
                childNodeIndex = len(self.dictGLTF["nodes"])
                self.dictGLTF["scenes"][0]["nodes"].append(childNodeIndex)

                self.dictGLTF["skins"][0]["joints"].append(childNodeIndex)
                self.dictGLTF["nodes"].append({
                    "name": tokens[1] # line.rfind(" ") + 1
                })
                
                self.hierarchyData["nodeDatas"].append(
                    dict(NodeData())
                )
                self.offset = self.offset + 1

                if(not self.generateHierarchy(childNodeIndex,currentMatrix)):
                    return False
                
                return True
            
            elif (tokens[0] == "JOINT"):
                childNodeIndex = len(self.dictGLTF["nodes"])

                if(not self.dictGLTF["nodes"][nodeIndex].__contains__("children")):
                    self.dictGLTF["nodes"][nodeIndex]["children"]=[]
                
                self.dictGLTF["nodes"][nodeIndex]["children"].append(childNodeIndex)
                self.dictGLTF["skins"][0]["joints"].append(childNodeIndex)
                
                self.dictGLTF["nodes"].append({
                    "name":  tokens[1] # line.substr(line.rfind(" ") + 1)
                })

                self.hierarchyData["nodeDatas"].append(dict(NodeData()))

                self.offset = self.offset + 1

                if(not self.generateHierarchy(childNodeIndex,currentMatrix)):
                    return False
            # elif (line.rfind("End Site", 0) == 0):
            elif (tokens[0]=="End" and tokens[1] == "Site"):

                childNodeIndex = len(self.dictGLTF["nodes"])
                
                if(not self.dictGLTF["nodes"][nodeIndex].__contains__("children")):
                    self.dictGLTF["nodes"][nodeIndex]["children"] = []
                
                self.dictGLTF["nodes"][nodeIndex]["children"].append(childNodeIndex)
                self.dictGLTF["skins"][0]["joints"].append(childNodeIndex)
                
                self.dictGLTF["nodes"].append({
                    "name": self.dictGLTF["nodes"][nodeIndex]["name"] + " End"
                })

                self.hierarchyData["nodeDatas"].append(dict(NodeData()))
                self.offset = self.offset + 1

                if(not self.generateHierarchy(childNodeIndex,currentMatrix)):
                    return False

            # elif (line.rfind("{", 0) == 0):
            elif (tokens[0] == "{"):

                self.offset = self.offset + 1
                print("Info: Entering node %s \n" %(self.dictGLTF["nodes"][nodeIndex]["name"]))
            # elif (line.rfind("OFFSET", 0) == 0):

            elif (tokens[0] == "OFFSET"):
                
                self.offset = self.offset + 1
                # from scanf import scanf
                # tmp = scanf("%s %f %f %f", trim(line))
                # print("OFFSET==line==>", line, tmp,trim(line))
                # buffer = tmp[0]
                # x = tmp[1]
                # y=tmp[2]
                # z=tmp[3]
                buffer = tokens[0]
                x = float(tokens[1])
                y = float(tokens[2])
                z = float(tokens[3])

                self.dictGLTF["nodes"][nodeIndex]["translation"] = [x,y,z]

                currentMatrix = parentMatrix * glm.translate(glm.mat4(1.0), glm.vec3(x,y,z))
                # print("Info: Node %s")
            # elif (line.rfind("CHANNELS", 0) == 0):
            elif (tokens[0] == "CHANNELS"):

                self.offset = self.offset + 1
                # stringStream = StringIO(line)
                # currentToken = 0
                # line = CHANNELS 3 Zrotation Xrotation Yrotation
                # 
                subtokens = trim(line).split(" ")
                currentTokenIndex = 0
                while(currentTokenIndex in range(len(subtokens))):
                    print("subtokens currentTokenIndex==>", subtokens[currentTokenIndex])
                    if(currentTokenIndex == 1):
                        currentChannels = subtokens[currentTokenIndex]
                        print("Info:Node %s has %s channels \n" %(self.dictGLTF["nodes"][nodeIndex]["name"], currentChannels))
                    if(currentTokenIndex >= 2):
                        token = subtokens[currentTokenIndex]

                        if(token =="Xposition" or token == "Yposition" or token == "Zposition"):
                            
                            print("====>", self.hierarchyData["nodeDatas"][nodeIndex]["positionChannels"], token)
                            self.hierarchyData["nodeDatas"][nodeIndex]["positionChannels"].append(token)
                        
                        elif(token == "Xrotation" or token == "Yrotation" or token == "Zrotation"):
                            print("====>", self.hierarchyData["nodeDatas"][nodeIndex]["rotationChannels"])
                            self.hierarchyData["nodeDatas"][nodeIndex]["rotationChannels"].append(token)
                        
                        else:
                            print("Unkown (HIERARCHY) token %s \n" %(token))
                            return False
                    currentTokenIndex = currentTokenIndex + 1

            # elif (line.rfind("}", 0) == 0):
            elif (tokens[0] == "}"):

                self.offset = self.offset + 1

                inverseMatrix = glm.inverse(parentMatrix)
                # print("****",glm.value_ptr(inverseMatrix))
                self.byteData = self.byteData + inverseMatrix.to_bytes() #glm.value_ptr(inverseMatrix)

                print("Info: Leaving node %s \n" %(self.dictGLTF["nodes"][nodeIndex]["name"]))
                return True
            else:
                print("***", tokens)
                print("Error: Unknown in HIERARCHY %s\n" %line)
                return False

        return True
    
    # motion data 
    def gatherSamples(self):
        """
        TODO:实际调用案例
        """
        # motionData = self.motionData
        # offset = self.offset
        # bvhLines = self.bvhLines

        currentFrame = 0

        while(self.offset < len(self.bvhLines)):
            line = self.bvhLines[self.offset]
            
            self.offset = self.offset + 1
            
            tokens = trim(line).split(" ")
            
            token = ""
            values = []
            for token in tokens:
                # self.motionData["frameDatas"][currentFrame]["values"].append(token)
                values.append(float(token))

            self.motionData["frameDatas"].append({
                "values": values
            })
            # print("samples::::", self.motionData)
            # print("Info: Frame %zu has %zu samples \n" %(currentFrame, len(motionData["frameDatas"][currentFrame]["values"])))
            currentFrame = currentFrame + 1
        return True

    def generateMotion( self ):
        """
        Frames:    2
        Frame Time: 0.033333
        8.03	 35.01	 88.36	-3.41	 14.78	-164.35	 13.09	 40.30	-24.60	 7.88	 43.80	 0.00	-3.61	-41.45	 5.82	 10.08	 0.00	 10.21	 97.95	-23.53	-2.14	-101.86	-80.77	-98.91	 0.69	 0.03	 0.00	-14.04	 0.00	-10.50	-85.52	-13.72	-102.93	 61.91	-61.18	 65.18	-1.57	 0.69	 0.02	 15.00	 22.78	-5.92	 14.93	 49.99	 6.60	 0.00	-1.14	 0.00	-16.58	-10.51	-3.11	 15.38	 52.66	-21.80	 0.00	-23.95	 0.00	
        7.81	 35.10	 86.47	-3.78	 12.94	-166.97	 12.64	 42.57	-22.34	 7.67	 43.61	 0.00	-4.23	-41.41	 4.89	 19.10	 0.00	 4.16	 93.12	-9.69	-9.43	 132.67	-81.86	 136.80	 0.70	 0.37	 0.00	-8.62	 0.00	-21.82	-87.31	-27.57	-100.09	 56.17	-61.56	 58.72	-1.63	 0.95	 0.03	 13.16	 15.44	-3.56	 7.97	 59.29	 4.97	 0.00	 1.64	 0.00	-17.18	-10.02	-3.08	 13.56	 53.38	-18.07	 0.00	-25.93	 0.00	

        """
        # hierarchyData = self.hierarchyData
        # motionData = self.motionData
        # offset = self.offset
        # bvhLines = self.bvhLines

        while(self.offset < len(self.bvhLines)):
            line = self.bvhLines[self.offset]
            tokens = trim(line).split(":")

            if(tokens[0] == "Frames"):
                self.motionData["frames"] = int(tokens[1])
                # 分配motionData.frameDatas长度为frames
                self.offset = self.offset + 1
            elif(tokens[0] == "Frame Time" ):
                # 帧时长
                self.motionData["frameTime"] = float(tokens[1])

                self.offset = self.offset + 1
                # 开始处理具体得动作数据
                if(not self.gatherSamples()):
                    return False
                return True
            else:
                print("Error: Unkown in Motion %s \n" %(line))
                return False
        return True
    def generate( self ):
        """

        """
        # offset = 0
        # dictGLTF = self.dictGLTF
        # byteData = self.byteData
        # hierarchyData = self.hierarchyData
        # motionData = self.motionData
        # offset = self.offset
        # bvhLines = self.bvhLines

        while (self.offset < len(self.bvhLines)):
            
            line = trim(self.bvhLines[self.offset])
            

            if(line == "HIERARCHY"):
                print("generate HIERARCHY =====>", self.offset, line)
                self.offset = self.offset + 1
                if(not self.generateHierarchy(0,glm.mat4(1.0))):
                    return False
            elif (line == "MOTION"):
                print("generate HIERARCHY =====>", self.offset, line)
                self.offset = self.offset + 1
                
                if(not self.generateMotion()):
                    return False
            else:
                self.offset = self.offset + 1
                print("Error: Unkown %s at line %d" %(line, self.offset))

        return True
    
    def gatherLines(self):
        """
        parse bvh data to bvhLines
        """
        stringStream = StringIO(self.bvhContent)
        self.bvhLines = []
        while True:
            line = stringStream.readline()
            if line == '':
                break
            self.bvhLines.append(line)
        print("gatherLines===>", len(self.bvhLines))

    def convert(self,bvhFileName,saveGltfName,saveBinaryName):
        self.bvhFileName = bvhFileName
        self.saveGltfName = saveGltfName
        self.saveBinaryName = saveBinaryName

        # load bvh file
        if( not self.loadFile(bvhFileName)):
            print("Error: Could not load BVH file %s" %(bvhFilename))
            return False
        print("Info: Loaded BVH %s" %(bvhFileName))

        # gather lines from bvhContent
        self.gatherLines()

        # glTF setup
        self.initGLTF()

        # generate all data for gltf
        if (not self.generate()):
            print("Error: Could not convert BVH to gltf\n")
            return False
        # check the result from generate method
        print("generate:::", self.motionData)
        # Sorting data per node,target position and rotation
        currentDataIndex = 0
        for currentFrameIndex in  range(self.motionData["frames"]):
            currentDataIndex = 0

            for currentNodeIndex in range(len(self.hierarchyData["nodeDatas"])):
                currentNode = self.hierarchyData["nodeDatas"][currentNodeIndex]
                for p in range(len(currentNode["positionChannels"])):
                    currentNode["positionData"].append(
                        self.motionData["frameDatas"][currentFrameIndex]["values"][currentDataIndex]
                    )
                    currentDataIndex = currentDataIndex + 1

                for r in range(len(currentNode["rotationChannels"])):
                    currentNode["rotationData"].append(
                        self.motionData["frameDatas"][currentFrameIndex]["values"][currentDataIndex]
                    )                    
                    currentDataIndex = currentDataIndex + 1
        
        data = b""
        byteLength = 0
        byteOffset = 0
        data = data + copy.deepcopy(self.byteData)
        byteOffset = len(data)
        byteLength = len(data)
        

        self.dictGLTF['bufferViews'][0]['byteLength']=len(data)
        self.dictGLTF['accessors'][0]['count']=len(self.dictGLTF['nodes'])
        
        

        # key frames
        # keyframes = list(range(self.motionData["frames"]))        
        keyframes = []

        for i in range(self.motionData["frames"]):
            # keyframes[i] = self.motionData["frameTime"] * 4 #float占用字节数=8
            keyframes.append(self.motionData["frameTime"] * 4)

        bufferViewIndex = len(self.dictGLTF['bufferViews'])
        self.dictGLTF["bufferViews"].append({
            "buffer":0,
            "byteOffset": byteOffset,
            "byteLength": self.motionData["frames"] * 4 # sizeof(float)
        })

        accessorIndex = len(self.dictGLTF["accessors"])
        self.dictGLTF["accessors"].append({
            "bufferView":bufferViewIndex,
            "componentType":5126,
            "count": self.motionData["frames"],
            "type":"SCALAR",
            "min": [keyframes[0]],
            "max": [keyframes[len(keyframes)-1]]

        })

        
        # data = data + bytes(copy.deepcopy(keyframes))
        bb = array_to_bytes(keyframes, "f")
        data = data + bb
        byteOffset = len(data)
        byteLength = len(data)
        # 
        inputAccessorIndex = accessorIndex
        animationSamplerIndex = 0
        animationChannelIndex = 0

        # Generate animations, as we now do have all the data sorted out.
        for currentNodeIndex in range(len(self.hierarchyData["nodeDatas"])):
            currentNode = self.hierarchyData["nodeDatas"][currentNodeIndex]
            
            if(len(currentNode["positionChannels"]) > 0):

                bufferViewIndex = len(self.dictGLTF["bufferViews"])

                self.dictGLTF["bufferViews"].append({
                    "buffer": 0,
                    "byteOffset": byteOffset,
                    "byteLength": self.motionData["frames"] * 3 * 4 #sizeof(float)
                })

                accessorIndex = len(self.dictGLTF["accessors"])

                self.dictGLTF["accessors"].append({
                    "bufferView": bufferViewIndex,
                    "componentType": 5126,
                    "count":  self.motionData["frames"],
                    "type":"VEC3"
                })

                # 
                finalPositionData = []
                for currentFrameIndex in range(self.motionData["frames"]):
                    for i in range(len(currentNode["positionChannels"])):
                        if (currentNode["positionChannels"][i] == "Xposition"):
                            # finalPositionData[currentFrameIndex*3 + 0] = currentNode["positionData"][currentFrameIndex * len(currentNode["positionChannels"]) + i]
                            finalPositionData.append(currentNode["positionData"][currentFrameIndex * len(currentNode["positionChannels"]) + i])
                        elif (currentNode["positionChannels"][i] == "Yposition"):
                            # finalPositionData[currentFrameIndex*3 + 1] = currentNode.positionData[currentFrameIndex * currentNode.positionChannels.size() + i]
                            finalPositionData.append(currentNode["positionData"][currentFrameIndex * len(currentNode["positionChannels"]) + i])
                        elif (currentNode["positionChannels"][i] == "Zposition"):
                            # finalPositionData[currentFrameIndex*3 + 2] = currentNode["positionData"][currentFrameIndex * len(currentNode["positionChannels"]) + i]
                            finalPositionData.append(currentNode["positionData"][currentFrameIndex * len(currentNode["positionChannels"]) + i])

                print("finalPositionData==>", finalPositionData)
                data = data + array_to_bytes(finalPositionData,"f")
                byteOffset = len(data)
                byteLength = len(data)

                # 
                animationSamplerIndex = len(self.dictGLTF["animations"][0]["samplers"])
                animationChannelIndex = len(self.dictGLTF["animations"][0]["channels"])

                self.dictGLTF["animations"][0]["samplers"].append({
                    "input": inputAccessorIndex,
                    "interpolation": "LINEAR",
                    "output": accessorIndex
                })

                self.dictGLTF["animations"][0]["channels"].append({
                    "sampler": animationSamplerIndex,
                    "target":{
                        "path": "translation",
                        "node":currentNodeIndex
                    },
                })
            if(len(currentNode["rotationChannels"]) >0):

                bufferViewIndex = len(self.dictGLTF["bufferViews"])
                
                self.dictGLTF["bufferViews"].append({
                    "buffer": 0,
                    "byteOffset": byteOffset,
                    "byteLength": self.motionData["frames"] * 4 * 4 # sizeof(float)
                })

                # 
                accessorIndex = len(self.dictGLTF["accessors"])
                self.dictGLTF["accessors"].append({
                    "bufferView": bufferViewIndex,
                    "componentType": 5126,
                    "count": self.motionData["frames"],
                    "type": "VEC4"
                })

                # 

                finalRotationData = []
                for currentFrameIndex in range(self.motionData["frames"]):

                    matrix = glm.mat4(1.0)
                    
                    for i in range(len(currentNode["rotationChannels"])):

                        angle = currentNode["rotationData"][currentFrameIndex * len(currentNode["rotationChannels"]) + i]
                        
                        if(currentNode["rotationChannels"][i] == "Xposition"):
                            matrix = matrix * glm.rotate(glm.radians(angle), glm.vec3(1.0,0.0,0.0))
                        elif (currentNode["rotationChannels"][i] == "Yposition"):
                            matrix = matrix * glm.rotate(glm.radians(angle), glm.vec3(0.0,1.0,0.0))
                        elif (currentNode["rotationChannels"][i] == "Zrotation"):
                            matrix = matrix * glm.rotate(glm.radians(angle), glm.vec3(0.0,0.0,1.0))
                    
                    rotation = glm.quat_cast(matrix)
                    # finalRotationData.append(currentFrameIndex * 4 + 0, rotation.x)
                    # finalRotationData.append(currentFrameIndex * 4 + 1, rotation.y)
                    # finalRotationData.append(currentFrameIndex * 4 + 2, rotation.z)
                    # finalRotationData.append(currentFrameIndex * 4 + 3, rotation.w)
                    finalRotationData.append(rotation[0])
                    finalRotationData.append(rotation[1])
                    finalRotationData.append(rotation[2])
                    finalRotationData.append(rotation[3])
                    
                # 
                
                data = data + array_to_bytes(finalRotationData,"f")
                byteOffset = len(data)
                byteLength = len(data)

                animationChannelIndex = len(self.dictGLTF["animations"][0]["channels"])
                animationSamplerIndex = len(self.dictGLTF["animations"][0]["samplers"])

                self.dictGLTF["animations"][0]["samplers"].append({
                    "input": inputAccessorIndex,
                    "interpolation": "LINEAR",
                    "output": accessorIndex
                })

                self.dictGLTF["animations"][0]["channels"].append({
                    "sampler":animationSamplerIndex,
                    "target": {
                        "path": "rotation",
                        "node": currentNodeIndex
                    }
                })
            
        
        nodeIndex = len(self.dictGLTF["nodes"])
        self.dictGLTF["scenes"][0]["nodes"].append(nodeIndex)

        self.dictGLTF["nodes"].append({
            "name": "Mesh",
            "skin": 0
        })
        self.dictGLTF["buffers"][0]["byteLength"] = byteLength

        # print("data==>", data)
        # print("data==>", "".join(data))
        # Saving everything
        if not self.saveFile(data, self.saveBinaryName):
            print("Error: Could not save generated bin file %s\n", self.saveBinaryName)
            return False
        if not self.saveFile(json.dumps(self.dictGLTF),self.saveGltfName, "w"):
            print("Error: Could not save generated gltf file %s", self.saveGltfName)
            return False

        print("Info: Saved glTF %s\n" %(self.saveGltfName))
        return True            

if __name__ == "__main__":
    bvhTool = BvhTool()
    bvhTool.convert("./Example1.bvh", "./untitled.gltf", "untitled.bin")
