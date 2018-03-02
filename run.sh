python run.py
TIME=$(date +%Y.%m.%d\(%H.%M.%S\))
LOG_DIR='/home/admin/imtMonitor'
mkdir -p ${LOG_DIR}
LOG_FILE='log.out'
echo $TIME' 监工执行完成' >> ${LOG_DIR}/${LOG_FILE}