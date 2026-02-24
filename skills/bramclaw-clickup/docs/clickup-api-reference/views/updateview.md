# Update View

Rename a view, update the grouping, sorting, filters, columns, and settings of a view.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/view/{view_id}": {
      "put": {
        "summary": "Update View",
        "tags": [
          "Views"
        ],
        "description": "Rename a view, update the grouping, sorting, filters, columns, and settings of a view.",
        "operationId": "UpdateView",
        "parameters": [
          {
            "name": "view_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "3c"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateViewrequest",
                "required": [
                  "name",
                  "type",
                  "parent",
                  "grouping",
                  "divide",
                  "sorting",
                  "filters",
                  "columns",
                  "team_sidebar",
                  "settings"
                ],
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "parent": {
                    "title": "Parent",
                    "description": "The parent parameter specifies where the view is located in the ClickUp Hierarchy. Both `id` and `type` are required. \\\n \\\nThe `id` is the id of the Workspace, Space, Folder, or List where the view is located. \\\n \\\nThe `type` value indciates the level of the Hierarchy where the view is located.",
                    "required": [
                      "id",
                      "type"
                    ],
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "The id of the Workspace, Space, Folder, or List where the view is located."
                      },
                      "type": {
                        "type": "integer",
                        "description": "The level of the Hierarchy where the view is created. \\\n \\\nOptions include: \\\n \\\nWorkspace (Everything Level): `7` \\\n \\\nSpace: `4` \\\n \\\nFolder: `5` \\\n \\\nList: `6`",
                        "contentEncoding": "int32"
                      }
                    },
                    "examples": [
                      {
                        "id": "512",
                        "type": 7
                      }
                    ]
                  },
                  "grouping": {
                    "title": "Grouping",
                    "required": [
                      "field",
                      "dir",
                      "collapsed",
                      "ignore"
                    ],
                    "type": "object",
                    "properties": {
                      "field": {
                        "type": "string",
                        "description": "Set the field to group by.\\\n \\\nOptions include: `none`, `status`, `priority`, `assignee`, `tag`, or `dueDate`."
                      },
                      "dir": {
                        "description": "Set a group sort order using `1` or `-1`.\\\n \\\nFor example, use `1`show tasks with urgent priority at the top of your view, and tasks with no priority at the bottom.\\\n \\\nUse `-1` to reverse the order to show tasks with no priority at the top of your view.",
                        "type": "integer",
                        "contentEncoding": "int32"
                      },
                      "collapsed": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": ""
                      },
                      "ignore": {
                        "type": "boolean"
                      }
                    },
                    "examples": [
                      {
                        "field": "status",
                        "dir": 1,
                        "collapsed": [],
                        "ignore": false
                      }
                    ]
                  },
                  "divide": {
                    "title": "Divide",
                    "required": [
                      "collapsed"
                    ],
                    "type": "object",
                    "properties": {
                      "field": {
                        "type": [
                          "null"
                        ]
                      },
                      "dir": {
                        "type": [
                          "null"
                        ]
                      },
                      "collapsed": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "examples": [
                      {
                        "field": null,
                        "dir": null,
                        "collapsed": []
                      }
                    ]
                  },
                  "sorting": {
                    "title": "Sorting",
                    "required": [
                      "fields"
                    ],
                    "type": "object",
                    "properties": {
                      "fields": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "Include an array of fields to sort by.\\\n \\\n You can sort by the same fields available when [filtering a view](https://developer.clickup.com/docs/filter-views)."
                      }
                    },
                    "examples": [
                      {
                        "fields": [
                          {
                            "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                            "dir": -1,
                            "idx": 0
                          }
                        ]
                      }
                    ]
                  },
                  "filters": {
                    "title": "Filters",
                    "required": [
                      "op",
                      "fields",
                      "search",
                      "show_closed"
                    ],
                    "type": "object",
                    "properties": {
                      "op": {
                        "type": "string",
                        "description": "The available operator (`op``) values are `AND`` and `OR``."
                      },
                      "fields": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": "View the list of [fields available](https://developer.clickup.com/docs/filter-views) to filter by."
                      },
                      "search": {
                        "type": "string"
                      },
                      "show_closed": {
                        "type": "boolean"
                      }
                    },
                    "examples": [
                      {
                        "op": "AND",
                        "fields": [],
                        "search": "",
                        "show_closed": false
                      }
                    ]
                  },
                  "columns": {
                    "title": "Columns",
                    "description": "Custom Fields added to a view at the Everything level will be added to all tasks in your Workspace. Once Custom Fields are added to one of these views, you cannot move it to another level of the Hierarchy.",
                    "required": [
                      "fields"
                    ],
                    "type": "object",
                    "properties": {
                      "fields": {
                        "description": "Custom Fields require the `cf_` prefix and must be formatted as a JSON object. Example: `cf_eb1234567890-c676-4c10-9012-345678901234`",
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "examples": [
                      {
                        "fields": []
                      }
                    ]
                  },
                  "team_sidebar": {
                    "title": "TeamSidebar",
                    "required": [
                      "assignees",
                      "assigned_comments",
                      "unassigned_tasks"
                    ],
                    "type": "object",
                    "properties": {
                      "assignees": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        },
                        "description": ""
                      },
                      "assigned_comments": {
                        "type": "boolean"
                      },
                      "unassigned_tasks": {
                        "type": "boolean"
                      }
                    },
                    "examples": [
                      {
                        "assignees": [],
                        "assigned_comments": false,
                        "unassigned_tasks": false
                      }
                    ]
                  },
                  "settings": {
                    "title": "Settings",
                    "required": [
                      "show_task_locations",
                      "show_subtasks",
                      "show_subtask_parent_names",
                      "show_closed_subtasks",
                      "show_assignees",
                      "show_images",
                      "collapse_empty_columns",
                      "me_comments",
                      "me_subtasks",
                      "me_checklists"
                    ],
                    "type": "object",
                    "properties": {
                      "show_task_locations": {
                        "type": "boolean"
                      },
                      "show_subtasks": {
                        "description": "Acceptable values are `1`, `2`, or `3`, which show subtasks separate, expanded, or collapsed.",
                        "type": "integer",
                        "contentEncoding": "int32"
                      },
                      "show_subtask_parent_names": {
                        "type": "boolean"
                      },
                      "show_closed_subtasks": {
                        "type": "boolean"
                      },
                      "show_assignees": {
                        "type": "boolean"
                      },
                      "show_images": {
                        "type": "boolean"
                      },
                      "collapse_empty_columns": {
                        "type": [
                          "string",
                          "null"
                        ]
                      },
                      "me_comments": {
                        "type": "boolean"
                      },
                      "me_subtasks": {
                        "type": "boolean"
                      },
                      "me_checklists": {
                        "type": "boolean"
                      }
                    },
                    "examples": [
                      {
                        "show_task_locations": false,
                        "show_subtasks": 3,
                        "show_subtask_parent_names": false,
                        "show_closed_subtasks": false,
                        "show_assignees": true,
                        "show_images": true,
                        "collapse_empty_columns": null,
                        "me_comments": true,
                        "me_subtasks": true,
                        "me_checklists": true
                      }
                    ]
                  }
                },
                "examples": [
                  {
                    "name": "New View Name",
                    "type": "list",
                    "parent": {
                      "id": "512",
                      "type": 7
                    },
                    "grouping": {
                      "field": "status",
                      "dir": 1,
                      "collapsed": [],
                      "ignore": false
                    },
                    "divide": {
                      "field": null,
                      "dir": null,
                      "collapsed": []
                    },
                    "sorting": {
                      "fields": []
                    },
                    "filters": {
                      "op": "AND",
                      "fields": [],
                      "search": "",
                      "show_closed": false
                    },
                    "columns": {
                      "fields": []
                    },
                    "team_sidebar": {
                      "assignees": [],
                      "assigned_comments": false,
                      "unassigned_tasks": false
                    },
                    "settings": {
                      "show_task_locations": false,
                      "show_subtasks": 3,
                      "show_subtask_parent_names": false,
                      "show_closed_subtasks": false,
                      "show_assignees": true,
                      "show_images": true,
                      "collapse_empty_columns": null,
                      "me_comments": true,
                      "me_subtasks": true,
                      "me_checklists": true
                    }
                  }
                ]
              },
              "example": {
                "name": "New View Name",
                "type": "list",
                "parent": {
                  "id": "512",
                  "type": 7
                },
                "grouping": {
                  "field": "status",
                  "dir": 1,
                  "collapsed": [],
                  "ignore": false
                },
                "divide": {
                  "field": null,
                  "dir": null,
                  "collapsed": []
                },
                "sorting": {
                  "fields": [
                    {
                      "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                      "dir": -1,
                      "idx": 0
                    }
                  ]
                },
                "filters": {
                  "op": "AND",
                  "fields": [
                    {
                      "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                      "op": "EQ",
                      "determinor": null,
                      "idx": 0,
                      "values": "123"
                    }
                  ],
                  "search": "",
                  "show_closed": false
                },
                "columns": {
                  "fields": [
                    {
                      "field": "assignee",
                      "idx": 0,
                      "width": 160,
                      "hidden": true,
                      "name": null,
                      "display": null
                    }
                  ]
                },
                "team_sidebar": {
                  "assignees": [],
                  "assigned_comments": false,
                  "unassigned_tasks": false
                },
                "settings": {
                  "show_task_locations": false,
                  "show_subtasks": 3,
                  "show_subtask_parent_names": false,
                  "show_closed_subtasks": false,
                  "show_assignees": true,
                  "show_images": true,
                  "collapse_empty_columns": null,
                  "me_comments": true,
                  "me_subtasks": true,
                  "me_checklists": true
                }
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "UpdateViewresponse",
                  "required": [
                    "view"
                  ],
                  "type": "object",
                  "properties": {
                    "view": {
                      "title": "View"
                    }
                  },
                  "examples": [
                    {
                      "view": {
                        "id": "3c-105",
                        "name": "New View Name",
                        "type": "list",
                        "parent": {
                          "id": "512",
                          "type": 7
                        },
                        "grouping": {
                          "field": "status",
                          "dir": 1,
                          "collapsed": [],
                          "ignore": false
                        },
                        "divide": {
                          "field": null,
                          "dir": null,
                          "collapsed": []
                        },
                        "sorting": {
                          "fields": []
                        },
                        "filters": {
                          "op": "AND",
                          "fields": [],
                          "search": "",
                          "show_closed": false
                        },
                        "columns": {
                          "fields": []
                        },
                        "team_sidebar": {
                          "assignees": [],
                          "assigned_comments": false,
                          "unassigned_tasks": false
                        },
                        "settings": {
                          "show_task_locations": false,
                          "show_subtasks": 3,
                          "show_subtask_parent_names": false,
                          "show_closed_subtasks": false,
                          "show_assignees": true,
                          "show_images": true,
                          "collapse_empty_columns": null,
                          "me_comments": true,
                          "me_subtasks": true,
                          "me_checklists": true
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "view": {
                    "id": "3c-105",
                    "name": "New View Name",
                    "type": "list",
                    "parent": {
                      "id": "512",
                      "type": 7
                    },
                    "grouping": {
                      "field": "status",
                      "dir": 1,
                      "collapsed": [],
                      "ignore": false
                    },
                    "divide": {
                      "field": null,
                      "dir": null,
                      "collapsed": []
                    },
                    "sorting": {
                      "fields": [
                        {
                          "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                          "dir": -1,
                          "idx": 0
                        }
                      ]
                    },
                    "filters": {
                      "op": "AND",
                      "fields": [
                        {
                          "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                          "op": "EQ",
                          "determinor": null,
                          "idx": 0,
                          "values": "123"
                        }
                      ],
                      "search": "",
                      "show_closed": false
                    },
                    "columns": {
                      "fields": [
                        {
                          "field": "assignee",
                          "idx": 0,
                          "width": 160,
                          "hidden": true,
                          "name": null,
                          "display": null
                        }
                      ]
                    },
                    "team_sidebar": {
                      "assignees": [],
                      "assigned_comments": false,
                      "unassigned_tasks": false
                    },
                    "settings": {
                      "show_task_locations": false,
                      "show_subtasks": 3,
                      "show_subtask_parent_names": false,
                      "show_closed_subtasks": false,
                      "show_assignees": true,
                      "show_images": true,
                      "collapse_empty_columns": null,
                      "me_comments": true,
                      "me_subtasks": true,
                      "me_checklists": true
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Views"
    }
  ]
}
```