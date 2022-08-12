class linearregression:
    def __init__(self,data):
            self.data=data
            
    def M_SLOPE(self,data):
        X=(len(data)*sum(data['XY'])-sum(data['X'])*sum(data['Y']))
        Y=(len(data)* sum(data['squar_X'])-(sum(data['X'])**2))
        M=X/Y
        return M
    
    def B(self,data):
        B=(sum(data['Y']) - M * sum(data['X']))/N
        return B
    
    def SLOPE(self,data):
        X=data['X']
        Y=[(M * X + B) for X in range(1,len(X)+1)]
        return Y
    
    def MSE(self,data):
        MSE=sum([(y_org - y_pred)**2 for y_org,y_pred in zip(data['Y'],data['Y_PRIDECT'])])/N
        return MSE
    
    def RMSE(self,data):
        RMSE=math.sqrt(sum([(y_org - y_pred)**2 for y_org,y_pred in zip(data['Y'],data['Y_PRIDECT'])])/N)
        return RMSE
    
    def MAE(self,data):
        MAE=abs(sum([(y_pred - y_mean ) for y_pred,y_mean in zip(data['Y_PRIDECT'],data['Y_MEAN'])]))/N
        return MAE
    
    def R2(self,data):
        R2=1-sum([(y_org - y_pred)**2 for y_org,y_pred in zip(data['Y'],data['Y_PRIDECT'])])/sum([(y_org - y_mean)**2 for y_org,y_mean in zip(data['Y'],data['Y_MEAN'])])
        return R2
    
