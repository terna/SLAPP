def checkVersion(version,name,k0,k1,k2):
      # managing the presence of strings as rc in the version components
      vv=version.split('.')
      try: v0 = int(vv[0])
      except:
              try: v0 = int(vv[0][0:2])
              except:
                  try: v0 = int(vv[0][0:1])
                  except:
                      print("error in lib",name,"not regular version number")
                      os.sys.exit(1)
      if v0>k0: return True

      if len(vv)>=2:
          try: v1 = int(vv[1])
          except:
              try: v1 = int(vv[1][0:2])
              except:
                  try: v1 = int(vv[1][0:1])
                  except:
                      print("error in lib",name,"not regular version number")
                      os.sys.exit(1)
          if v0==k0 and v1>k1: return True

      if len(vv)>=3:
          try: v2 = int(vv[2])
          except:
             try: v2 = int(vv[2][0:2])
             except:
                 try: v2 = int(vv[2][0:1])
                 except:
                     print("error in lib",name,"not regular version number")
                     os.sys.exit(1)
          if v0==k0 and v1==k1 and v2>=k2: return True

      # the sequence never succeded
      return False
