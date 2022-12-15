# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:05:29 2022

@author: Ly Thien
"""
import numpy as np
import pandas as pd


def pcambtsr(X, A):
    '''
    TSA Source code
    
    ###############
    INPUTS
    X: data matrix with NaNs for the missing data (Numpy array/ matrix)
    A: number of principal components
    
    ###############
    OUTPUTS
    X: original data set with the imputed values
    m: estimated mean vector of X
    S: estimated covariance matrix of X
    It: number of iterations
    Xrec: PCA reconstruction of X with A components.
    '''
    X = pd.DataFrame(X)    
    n, p = X.shape
    df = [[0 for i in range(4)] for j in range(n)]
    df = pd.DataFrame(df, columns=["O", "M", "nO", "nM"])
    df = df.astype(object)
    for i in range(n-1, -1, -1):
            r = np.multiply(X.iloc[i,:].notna(), 1)
            df.iloc[i,0] = np.where(r == 1)[0]
            df.iloc[i,1] = np.where(r == 0)[0]
            df.iloc[i,2] = len(np.where(r == 1)[0])
            df.iloc[i,3] = len(np.where(r == 0)[0])
                
    # Adding mis variable:
    mis = np.multiply(X.isna(), 1)
    
    # Imput missing values for X with mean of each column:
    X = X.fillna(X.mean())
    
    maxiter = 5000
    conv = 1.0e-10
    diff = 100
    It = 0
    
    while It  < maxiter and diff > conv:
        It += 1
        Xmis = [X.iloc[i,j] for i in range(n) for j in range(p) if mis.iloc[i,j] == 1]
        mX = X.mean() #array mean after imputation
        S = X.cov()
        Xc = X - np.ones((n,p)) * mX.to_numpy()
        if n >p:
            U, D, V = np.linalg.svd(Xc)
        else:
            V, D, U = np.linalg.svd(Xc.transpose())
        V = pd.DataFrame(V)
        V = V.iloc[:, 0:A]
        for i in range(n):  # for each row
            if df.iloc[i, 3] > 0: # if thilocere are missing values
                L = V.iloc[df.iloc[i,0], 0:min(A, df.iloc[i, 2])] # L is the key matrix
                S11 =  S.iloc[df.iloc[i, 0], df.iloc[i, 0]]
                S21 =  S.iloc[df.iloc[i, 1], df.iloc[i, 0]]
                z1  =  Xc.iloc[i, df.iloc[i, 0]].transpose()
                z2  =  S21 @ L @ np.linalg.pinv (L.transpose() @ S11 @ L) @ L.transpose() @z1
                Xc.iloc[i, df.iloc[i, 1]] = z2.transpose()
        X = Xc + np.ones((n,p)) * mX.to_numpy()
        d = np.square(np.array([X.iloc[i,j] for i in range(n) for j in range(p) if mis.iloc[i,j] == 1]) - np.array(Xmis))
        diff = np.mean(d)
    
    S = X.cov()
    m = np.mean(X)
    U, D, V = np.linalg.svd(S)
    V = pd.DataFrame(V)
    P = V.iloc[:, 0:A]
    T = (X - np.ones((n,p))*m.to_numpy()) @ P 
    Xrec = np.ones((n, p)) * m.to_numpy() + T@ P.transpose()
    return X , m, S, It, Xrec
                
        
        
        
    
    
            
            
    