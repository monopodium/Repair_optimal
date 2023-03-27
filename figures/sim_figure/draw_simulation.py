import sys

sys.path.append("draw_pic")
sys.path.append("/home/ms/Repair_optimal/prototype/cmake/build")
import Code_parameters

if __name__ == '__main__':
    print(Code_parameters.PlacementType)
    encoder = Code_parameters.CodePyInterface()
    encoder.CreateEncoder(Code_parameters.EncodeType.Xorbas)