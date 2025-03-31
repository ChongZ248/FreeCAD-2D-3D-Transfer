

import FreeCAD
import Mesh
import Part
import Draft


# 设置Pad的参数
pad_length = 5  # 凸起的厚度或高度
cellsize_x=20
cellsize_y=20


# 加载 STL 文件到文档中
step_path = u"S:/Thesis/2dto3d/Plate-MergedBody.step"
Part.open(step_path)
doc = FreeCAD.activeDocument()

imported_object = doc.Objects[-1]  # 假设最后一个对象是刚导入的STEP对象
part = imported_object
platename=part.Name

##确定是否需要微调
##translation_vector = FreeCAD.Vector(-20, 0, 0)
##part.Placement.move(translation_vector)
##doc.recompute()


# 假设'Body'是我们要复制、平移和旋转的体
original_body = doc.getObject(platename)
cloned_body = Draft.clone(original_body, False)
cloned_body.Label = "ClonedBody"
cloname1=cloned_body.Name

rotation_axis = FreeCAD.Vector(0, 1, 0)  # Z轴
rotation_center = FreeCAD.Vector(0, 0, 0)  # 旋转中心点
rotation_angle = 90  # 旋转角度
translation_vector = FreeCAD.Vector(0, 0, 0)
rotation = FreeCAD.Rotation(rotation_axis, rotation_angle)
cloned_body.Placement.Rotation = rotation
cloned_body.Placement.move(translation_vector)
doc.recompute()

original_body = doc.getObject(platename)
cloned_body = Draft.clone(original_body, False)
cloned_body.Label = "ClonedBody2"
cloname2=cloned_body.Name
translation_vector = FreeCAD.Vector(0, 0,0)
cloned_body.Placement.move(translation_vector)
doc.recompute()


# 获取个体
body1 = doc.getObject(cloname1)  # 确保对象名称与你的文档匹配
body2 = doc.getObject(cloname2)



result_shape = body1.Shape.fuse(body2.Shape)
final_shape=result_shape
# final_shape = result_shape.fuse(body4.Shape)
merged_body = FreeCAD.ActiveDocument.addObject("Part::Feature", "MergedBody")
merged_body.Shape = final_shape
doc.recompute()

objs=[]
objs.append(doc.getObject("MergedBody"))
import Mesh
Mesh.export(objs,u"S:/Thesis/2dto3d/3D_Plate_B.stl")