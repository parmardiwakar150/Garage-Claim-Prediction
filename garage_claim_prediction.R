library(readxl)
data_mar = read_excel('Mplus Claim MAR-18.xlsx')
data_feb = read_excel('Mplus Claim FEB-2018.xlsx')
data_jan = read_excel('Claims JAN-2018.xlsx')
data_dec = read_excel('Claim DEC-2017.xlsx')
data_nov = read_excel('Claims NOV-2017.xlsx')
data_oct = read_excel('claims OCT-2017.xlsx')


dm = data_mar[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
              'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]
df = data_feb[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
                 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]
dj = data_jan[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
                 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]
dd = data_dec[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
                 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]
dn = data_nov[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
                 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]
do = data_oct[,c('PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt',
                 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo')]

dm$TotalClaim = dm$EstimateDentingAmt + dm$EstimatePaintingAmt + dm$EstimatePartRate + dm$EstimateRRAmt
df$TotalClaim = df$EstimateDentingAmt + df$EstimatePaintingAmt + df$EstimatePartRate + df$EstimateRRAmt
dj$TotalClaim = dj$EstimateDentingAmt + dj$EstimatePaintingAmt + dj$EstimatePartRate + dj$EstimateRRAmt
dd$TotalClaim = dd$EstimateDentingAmt + dd$EstimatePaintingAmt + dd$EstimatePartRate + dd$EstimateRRAmt
dn$TotalClaim = dn$EstimateDentingAmt + dn$EstimatePaintingAmt + dn$EstimatePartRate + dn$EstimateRRAmt
do$TotalClaim = do$EstimateDentingAmt + do$EstimatePaintingAmt + do$EstimatePartRate + do$EstimateRRAmt

data = rbind(dm, df, dj, dd, dn, do)
data = data[!(is.na(data$ModelID)),]
