import re

# with open('./data/KDD_node_features', 'r') as f:
#     raw_node_f = f.read()
# file_name_list = re.findall(r'\d{7,8}\b', raw_node_f)
# print(file_name_list)

a = [10001128, 10005232, 10010518, 10011554, 10017791, 10038011, 10061437, 10078748, 10095848, 1009607, 10105197, 10151654, 10164574, 10181044, 10186200, 10193735, 10201372, 10201458, 10224533, 10236111, 10257235, 10269043, 10275752, 10284571, 10285045, 1028607, 10346388, 10351682, 10489135, 1049322, 10508839, 10514814, 10561862, 10597102, 10655059, 1071109, 10757352, 10837032, 10837037, 10843921, 10843923, 10903275, 1092205, 10925003, 1094028, 10940984, 1094423, 10971362, 11080150, 1110787, 11117574, 11134936, 11142969, 11213575, 11270958, 11279489, 11394822, 1141080, 11470328, 11482753, 11536257, 11539451, 11546904, 11626792, 11669627, 1167574, 1167595, 1167659, 11804378, 11842174, 1186368, 1195189, 11980488, 11981864, 1209092, 1220729, 1225233, 1239715, 1288009, 13035191, 13066434, 13083411, 1317160, 13194551, 13222302, 1342241, 13502551, 1353138, 1364456, 1364573, 1370349, 1374932, 13755742, 13755977, 13802275, 13808584, 13809567, 13928451, 14051997, 14058457, 14076694, 14125260, 14344924, 1473866, 1522729, 1523191, 2341962, 2353166, 2916145, 3568707, 3680878, 3744882, 3748056, 3769914, 3769919, 3779321, 3780602, 3785570, 3788999, 3792033, 3809174, 3816158, 3852549, 3858841, 3859887, 3869373, 3906628, 3908215, 3918474, 3920459, 3921987, 3929140, 3950072, 3951829, 3961369, 4002392, 4016160, 4031511, 4051385, 4056131, 4100505, 4186146, 4249633, 4270261, 4306370, 4324571, 4398213, 4413738, 4422616, 4453627, 4469535, 4504437, 4511305, 4604920, 4609403, 4677655, 4685648, 4697801, 4697802, 4700797, 4711482, 4713024, 4721679, 4738341, 4738342, 4739043, 4740231, 4766160, 4774319, 4794787, 4818705, 4882089, 4886672, 4916705, 4978533, 4980157, 5005014, 5014927, 5023118, 5070260, 5097759, 5133167, 5143105, 5169771, 5228328, 5329968, 5446340, 6158185, 6259100, 6383098, 7101956, 7176671, 7833205, 9050379, 9060690, 9101741, 9102538, 9109385, 9111641, 9125701, 9133885, 9135998, 9142727, 9151050, 9161791, 9167777, 9194903, 9248967, 9251891, 9261711, 9274894, 9284044, 9309392, 9315193, 9336615, 9389455, 9403280, 9412373, 9419452, 9421192, 9463669, 9479071, 9485675, 9521135, 9605734, 9606991, 9611024, 9617212, 9618001, 9621454, 9624095, 9632155, 9640142, 9642833, 9647883, 9662316, 9663908, 9678724, 9683909, 9690351, 9692779, 9696778, 9701993, 9727373, 9729483, 9757313, 9759716, 9942032, 9942600, 9942601, 9944671, 9953918, 9962233, 9965882, 9972873, 9997445]
print(len(a))