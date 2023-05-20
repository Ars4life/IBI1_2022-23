from xml.dom.minidom import parse
import xml.dom.minidom
import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('GO', cell_overwrite_ok=True)
col = ['GO', 'name', 'definition', 'childnodes']
for i in range(0, 4):
    sheet.write(0, i, col[i])



DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
genes = collection.getElementsByTagName('term')


def findsubgene(geneid, total_list, pre_list):
    gene_subl = []
    for gene1 in total_list:
        gene_sup = gene1.getElementsByTagName('is_a')
        gene_id1 = gene1.getElementsByTagName('id')[0]
        gene_supid = []
        for i in range(0, len(gene_sup)):
            gene_supid.append(gene_sup[i].childNodes[0].data)
        if geneid in gene_supid:
            gene_subl.append(gene_id1.childNodes[0].data)
    for subgenes in gene_subl:
        if subgenes not in pre_list:
            pre_list.append(subgenes)
            findsubgene(subgenes, total_list, pre_list)
    return pre_list

count = 0
for gene0 in genes:
    gene_def = gene0.getElementsByTagName('def')[0]
    gene_defstr = gene_def.getElementsByTagName('defstr')[0].childNodes[0].data
    if gene_defstr.find('autophagosome') == -1:
        continue
    else:
        count += 1
        gene_id0 = gene0.getElementsByTagName('id')[0]
        gene_id = gene_id0.childNodes[0].data
        sheet.write(count, 0, gene_id)
        gene_name0 = gene0.getElementsByTagName('name')[0]
        gene_name = gene_name0.childNodes[0].data
        sheet.write(count, 1, gene_name)
        sheet.write(count, 2, gene_defstr)
        sub_gene_list = findsubgene(gene_id, genes, [])
        sheet.write(count, 3, len(sub_gene_list))

savepath = './GO1.xls'
book.save(savepath)




